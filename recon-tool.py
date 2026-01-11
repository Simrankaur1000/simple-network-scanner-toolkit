import sys
import os

# Check if tool name and target are provided
if len(sys.argv) < 3:
    print("Usage: python3 recon_tool.py <tool> <target>")
    print("Example: python3 recon_tool.py nmap 192.168.1.10")
    sys.exit(1)

tool = sys.argv[1]
target = sys.argv[2]

# Tool execution logic
if tool == "nmap":
    os.system(f"nmap {target}")

elif tool == "nikto":
    os.system(f"nikto -h {target}")

elif tool == "whatweb":
    os.system(f"whatweb {target}")

elif tool == "netdiscover":
    os.system(f"netdiscover -r {target}")

elif tool == "arp-scan":
    os.system(f"arp-scan {target}")

elif tool == "ping":
    os.system(f"ping -c 4 {target}")

elif tool == "traceroute":
    os.system(f"traceroute {target}")

elif tool == "nslookup":
    os.system(f"nslookup {target}")

elif tool == "dig":
    os.system(f"dig {target}")

elif tool == "nbtscan":
    os.system(f"nbtscan {target}")

elif tool == "smb":
    os.system(f"smbclient -L //{target} -N")

else:
    print("Tool not supported.")
    print("Supported tools:")
    print("nmap nikto whatweb netdiscover arp-scan ping")
    print("traceroute nslookup dig nbtscan smb")
