import socket

def scan_ports(target, start_port=1, end_port=100):
    print(f"Scanning {target} for open ports between {start_port}-{end_port}...")
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            try:
                s.send(b'\n')
                banner = s.recv(1024).decode().strip()
            except:
                banner = "Banner not available"
            print(f"Port {port}: OPEN | Service: {banner}")
        s.close()

if __name__ == "__main__":
    target = input("Enter target IP or domain: ")
    scan_ports(target)
