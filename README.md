# Simple Subnet Calculator

This is a simple command-line tool for calculating basic subnet information based on an IP address and CIDR mask.  
Built using Python's standard libraries (`ipaddress`).

## Features
- Calculate network address
- Calculate broadcast address
- Find first and last usable IP addresses
- Determine number of usable hosts

## Requirements
- Python 3.6 or higher

_No external libraries are required._

## Usage
1. Clone the repository:
```
git clone https://github.com/yourusername/subnetcalculator.git
```
2. Navigate to the project directory:

cd subnetcalculator

3. Run the program:

python main.py

## Example

Simple Subnet Calculator


Enter IP Address (e.g., 192.168.1.1): 192.168.1.100

Enter Subnet Mask (CIDR, e.g., 24): 24


Results:

Network Address: 192.168.1.0

Broadcast Address: 192.168.1.255

First Usable IP: 192.168.1.1

Last Usable IP: 192.168.1.254

Number of Usable Hosts: 254


## Future Improvements

- Add dotted-decimal subnet mask input (e.g., 255.255.255.0)
- Add IP address validation improvements
- Allow batch calculations
- (Optional) Rebuild GUI version once environment supports it

---

Built by LyricalEcho
