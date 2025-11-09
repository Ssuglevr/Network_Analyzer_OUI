#Network analyzer
import psutil
from scapy.all import ARP, Ether, srp
import requests
import ipaddress
import socket

def get_local_network():
    interfaces = psutil.net_if_addrs()
    for iface_name, iface_addresses in interfaces.items():
        for addr in iface_addresses:
            if addr.family == socket.AF_INET:
                ip = addr.address
                netmask = addr.netmask
                network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)
                return str(network)
    return None

def get_network_input():
    try:
        user_input = input("Introduce your network ip address  or press [ENTER] for use automatic ip: ").strip()
        if user_input:
            return user_input  
        else:
            return get_local_network()  
    except KeyboardInterrupt:
        print("Leaving of Network analyzer")

network = get_network_input()
devices = []

while True:
    print("--------------------------------------NETWORK ANALYZER--------------------------------------")
    print("Welcome to my little network analyzer, only gives ip, mac and manufacturer of network device")
    print("1. Start analysis ")
    print("2. Devices")
    print("3. Stop Network analyzer")

    try:
        op = int(input("Select your option: "))

        if op == 1:
            print(f"Scanning network: {network}")
            arp_request = ARP(pdst=network)
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = ether / arp_request
            result = srp(packet, timeout=10, verbose=False)[0]

            devices = []
            for sent, received in result:
                devices.append({'ip': received.psrc, 'mac': received.hwsrc})

            for device in devices:
                oui = device['mac'].upper().replace(":", "")[:6]
                url = f"https://api.macvendors.com/{oui}" 
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        manufacturer = response.text
                    else:
                        manufacturer = "Unknown"
                except Exception as e:
                    manufacturer = "Error fetching manufacturer"
            
                print(f"IP: {device['ip']} - MAC: {device['mac']} - Manufacturer: {manufacturer}")
        
        if op == 2:
            print("Devices detected:")
            for device in devices:
                print(f"IP: {device['ip']} - MAC: {device['mac']}")

        if op == 3:
            print("Stopping network analyzer.")
            break
    except KeyboardInterrupt:
        print("Leaving of Network analyzer")
        break
