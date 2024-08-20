README for assesment
Project Overview
This project contains a Python script for processing flow logs, specifically designed to parse and analyze log data based on predefined mappings in a lookup table. The script reads flow log data, applies tagging based on the destination port and protocol, and generates counts of each tag as well as each port/protocol combination found in the logs.

Features
Tag Assignment: Logs are tagged based on destination port and protocol using a lookup table.
Count Aggregation: The script counts occurrences of each tag and port/protocol combination.
Output Files: Results are written to a CSV file for easy viewing and analysis.
Assumptions
The log file (flow_logs.txt) and the lookup table (lookup_table.csv) must be in the same directory as the script.
The log file format assumes entries are space-separated and contain all expected fields.
The protocol in the lookup table is assumed to be either tcp, udp, or icmp.
No advanced libraries (e.g., Pandas, Spark) are used in this script; it relies solely on Python’s standard libraries (csv and collections).
Technologies Used
Python: The script is written in Python and uses standard libraries without dependence on external libraries such as Pandas or PySpark.


How to Run the Script
Ensure Python is Installed: Python 3.x is required to run the script.
Clone the Repository: Clone this repository to your local machine.

git clone <repository-url>

Navigate to the Script Directory:
cd path/to/script
Run the Script:
python pythonscript.py
Check Output:
The results will be output to output_counts.csv in the same directory.
File Descriptions
pythonscript.py: The main Python script that processes the flow logs.
flow_logs.txt: Sample flow log data.
lookup_table.csv: Lookup table for tagging based on port and protocol.