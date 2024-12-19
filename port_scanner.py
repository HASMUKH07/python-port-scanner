import socket
from datetime import datetime

def port_scanner(target, start_port, end_port):
    print(f"\nStarting scan on target: {target}")
    print(f"Scanning ports from {start_port} to {end_port}...\n")
    
    for port in range(start_port, end_port + 1):
        try:
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout for the connection
            sock.settimeout(0.5)
            # Try to connect to the target on the current port
            result = sock.connect_ex((target, port))
            
            if result == 0:
                print(f"Port {port} is OPEN")
            
            # Close the socket
            sock.close()
        except Exception as e:
            print(f"Error on port {port}: {e}")

if __name__ == "__main__":
    print("Welcome to the Python Port Scanner")
    
    # Input target
    target = input("Enter the target (IP or hostname): ")
    # Input port range
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    # Record the start time
    start_time = datetime.now()
    
    # Call the scanner function
    port_scanner(target, start_port, end_port)
    
    # Record the end time
    end_time = datetime.now()
    print(f"\nScan completed in: {end_time - start_time}")
