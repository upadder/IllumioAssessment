import csv
from collections import defaultdict
# File locations
lookup_filename = 'lookup_table.csv'
log_filename = 'flow_logs.txt'
output_filename = 'output_counts.csv'
def load_lookup_table(filename):
    lookup = {}
    with open(filename, mode='r', newline='', encoding='ascii') as file:
        reader = csv.reader(file)
        next(reader)  
        for dstport, protocol, tag in reader:
            key = (dstport.strip(), protocol.lower().strip())
            lookup[key] = tag.strip()
    return lookup

def parse_flow_logs(log_filename, lookup):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)
    untagged_count = 0

    with open(log_filename, mode='r', newline='', encoding='ascii') as file:
        for line in file:
            parts = line.strip().split()
            dstport = parts[5]
            protocol = 'tcp' if parts[7] == '6' else 'udp' if parts[7] == '17' else 'icmp' if parts[7] == '1' else 'unknown'
            protocol_key = protocol.lower()

            port_protocol_counts[(dstport, protocol_key)] += 1

            tag = lookup.get((dstport, protocol_key))
            if tag:
                tag_counts[tag] += 1
            else:
                untagged_count += 1

    return tag_counts, port_protocol_counts, untagged_count

def write_output(tag_counts, port_protocol_counts, untagged_count, output_filename):
    """ Write the counts to a CSV file. """
    with open(output_filename, mode='w', newline='', encoding='ascii') as file:
        writer = csv.writer(file)
        writer.writerow(['Tag Counts:'])
        writer.writerow(['Tag', 'Count'])
        for tag, count in tag_counts.items():
            writer.writerow([tag, count])
        writer.writerow(['Untagged', untagged_count])
        writer.writerow([])
        writer.writerow(['Port/Protocol Combination Counts:'])
        writer.writerow(['Port', 'Protocol', 'Count'])
        for (port, protocol), count in port_protocol_counts.items():
            writer.writerow([port, protocol, count])



# Main execution
lookup_table = load_lookup_table(lookup_filename)
tags, port_protocols, untagged = parse_flow_logs(log_filename, lookup_table)
write_output(tags, port_protocols, untagged, output_filename)

# Display the output CSV content
with open(output_filename, "r") as file:
    content = file.read()
    print(content)
