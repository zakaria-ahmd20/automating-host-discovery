import re
import os
network_address = input('what is your network address: ')
# Run Nmap
os.system(f'nmap -sn -PS21,22,25,80,445,3389,8080 -PU53,137,138 {network_address} -oN targets.txt')

# Regex for all IPs
ip_regex = r'\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}\b'

# Regex for IPs ending in .0
ip_ending_0_regex = re.compile(
    r'\b(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.'
    r'(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.'
    r'(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.0\b',
    re.MULTILINE
)

with open("targets.txt") as f, open("ips.txt", "w") as out:
    for line in f:
        match = re.search(ip_regex, line)
        if match:
            # skip if it matches .0
            if ip_ending_0_regex.search(line):
                print(f"Ignoring network address: {match.group()}")
                continue
            out.write(match.group() + "\n")
