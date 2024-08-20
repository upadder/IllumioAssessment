**README for assessment**
**Project Overview**
This project contains a Python script for processing flow logs, specifically designed to parse and analyze log data based on predefined mappings in a lookup table. The script reads flow log data, applies tagging based on the destination port and protocol, and generates counts of each tag as well as each port/protocol combination found in the logs.

**Features**
Tag Assignment: Logs are tagged based on the destination port and protocol using a lookup table.
Count Aggregation: The script counts occurrences of each tag and port/protocol combination.
Output Files: Results are written to a CSV file for easy viewing and analysis.


**Assumptions**
The log file (flow_logs.txt) and the lookup table (lookup_table.csv) must be in the same directory as the script.
The log file format assumes entries are space-separated and contain all expected fields.
The protocol in the lookup table is assumed to be either tcp, udp, or icmp.
No advanced libraries (e.g., Pandas, Spark) are used in this script; it relies solely on Python’s standard libraries (csv and collections).
Technologies Used
Python: The script is written in Python and uses standard libraries without dependence on external libraries such as Pandas or PySpark.
the program only supports default log format, not custom and the only version that is supported is 2. 


**How to Run the Script**
Ensure Python is Installed: Python 3.x is required to run the script.
Clone the Repository: Clone this repository to your local machine.

**git clone <repository-url>**

Navigate to the Script Directory:
**cd path/to/script**

Run the Script:
**python pythonscript.py**
**Check Output:**
The results will be output to output_counts.csv in the same directory.
File Descriptions
pythonscript.py: The main Python script that processes the flow logs.
flow_logs.txt: Sample flow log data.
lookup_table.csv: Lookup table for tagging based on port and protocol.

**Testing Data**
flow logs 
2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 6 25 20000 1620140761 1620140821 ACCEPT OK
2 123456789012 eni-4d3c2b1a 192.168.1.100 203.0.113.101 23 49154 6 15 12000 1620140761 1620140821 REJECT OK
2 123456789012 eni-5e6f7g8h 192.168.1.101 198.51.100.3 25 49155 6 10 8000 1620140761 1620140821 ACCEPT OK
2 123456789012 eni-9h8g7f6e 172.16.0.100 203.0.113.102 110 49156 6 12 9000 1620140761 1620140821 ACCEPT OK
2 123456789012 eni-7i8j9k0l 172.16.0.101 192.0.2.203 993 49157 6 8 5000 1620140761 1620140821 ACCEPT OK
2 123456789012 eni-6m7n8o9p 10.0.2.200 198.51.100.4 143 49158 6 18 14000 1620140761 1620140821 ACCEPT OK
2 123456789012 eni-1a2b3c4d 192.168.0.1 203.0.113.12 1024 80 6 10 5000 1620140661 1620140721 ACCEPT OK
2 123456789012 eni-1a2b3c4d 203.0.113.12 192.168.0.1 80 1024 6 12 6000 1620140661 1620140721 ACCEPT OK
2 123456789012 eni-1a2b3c4d 10.0.1.102 172.217.7.228 1030 443 6 8 4000 1620140661 1620140721 ACCEPT OK
2 123456789012 eni-5f6g7h8i 10.0.2.103 52.26.198.183 56000 23 6 15 7500 1620140661 1620140721 REJECT OK
2 123456789012 eni-9k10l11m 192.168.1.5 51.15.99.115 49321 25 6 20 10000 1620140661 1620140721 ACCEPT OK
2 123456789012 eni-1a2b3c4d 192.168.1.6 87.250.250.242 49152 110 6 5 2500 1620140661 1620140721 ACCEPT OK
2 123456789012 eni-2d2e2f3g 192.168.2.7 77.88.55.80 49153 993 6 7 3500 1620140661 1620140721 ACCEPT OK
2 123456789012 eni-4h5i6j7k 172.16.0.2 192.0.2.146 49154 143 6 9 4500 1620140661 1620140721 ACCEPT OK

**lookup table**
dstport	protocol	tag
25	tcp	sv_P1
68	udp	sv_P2
23	tcp	sv_P1
31	udp	SV_P3
443	tcp	sv_P2
22	tcp	sv_P4
3389	tcp	sv_P5
0	icmp	sv_P5
110	tcp	email
993	tcp	email
143	tcp	email

last the output 
Tag Counts:		
Tag	Count	
sv_P2	1	
sv_P1	2	
email	3	
Untagged	8	
		
Port/Protocol Combination Counts:		
Port	Protocol	Count
443	tcp	1
23	tcp	1
25	tcp	1
110	tcp	1
993	tcp	1
143	tcp	1
1024	tcp	1
80	tcp	1
1030	tcp	1
56000	tcp	1
49321	tcp	1
49152	tcp	1
49153	tcp	1
49154	tcp	1

