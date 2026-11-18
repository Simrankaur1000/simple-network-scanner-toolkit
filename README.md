# Network Reconnaissance & Enumeration Toolkit

A command-line wrapper that brings common network discovery, reconnaissance, and enumeration utilities together behind a single interface for Kali Linux.

## Supported utilities

- **Host and port discovery:** Nmap, Netdiscover, arp-scan, ping
- **Web assessment:** Nikto, WhatWeb
- **Network diagnostics:** traceroute, nslookup, dig
- **Windows / NetBIOS discovery:** nbtscan, SMB-related enumeration

## Usage

```bash
python3 recon_tool.py <tool> <target>
```

Examples:

```bash
python3 recon_tool.py nmap 192.0.2.10
python3 recon_tool.py nikto http://192.0.2.10
```

Use the exact tool names and argument format supported by the current script. The external utilities must be installed and available in your system PATH.

## Environment

- Kali Linux or another compatible Linux distribution
- Python 3
- Required utilities installed separately (Nmap, Nikto, WhatWeb, arp-scan, and others as needed)

## Workflow

1. Define an authorized target and scope.
2. Select the required discovery or enumeration utility.
3. Run the command and review its output.
4. Validate findings manually before reporting them.

## Safety

Use only against systems you own or have explicit permission to test. Do not scan public or third-party infrastructure without authorization.

## Author

Simran Kaur · [Portfolio](https://portfolio-k3wf.vercel.app)
