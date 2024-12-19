import socket
import threading
import logging
from datetime import datetime
import os

logging.basicConfig(filename="port_scanner.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port} is OPEN")
            logging.info(f"Port {port} is OPEN on {target}")
        
        sock.close()
    except socket.timeout:
        logging.warning(f"Timeout error on port {port} for {target}")
    except Exception as e:
        logging.error(f"Error on port {port}: {e}")

def port_scanner(target, start_port, end_port):
    print(f"\nStarting scan on target: {target}")
    print(f"Scanning ports from {start_port} to {end_port}...\n")

    threads = []
    
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def save_results(target, start_port, end_port):
    with open("scan_results.txt", "w") as file:
        file.write(f"Port scan results for {target} from port {start_port} to {end_port}\n")
        file.write("="*50 + "\n")
        with open("port_scanner.log", "r") as log_file:
            file.write(log_file.read())

if __name__ == "__main__":
    print("Welcome to the Advanced Python Port Scanner")
    
    target = input("Enter the target (IP or hostname): ")
    while True:
        try:
            start_port = int(input("Enter the start port: "))
            end_port = int(input("Enter the end port: "))
            if start_port < 1 or end_port > 65535 or start_port > end_port:
                raise ValueError
            break
        except ValueError:
            print("Please enter valid port numbers between 1 and 65535, with the start port less than or equal to the end port.")
    
    start_time = datetime.now()

    port_scanner(target, start_port, end_port)

    end_time = datetime.now()
    print(f"\nScan completed in: {end_time - start_time}")

    save_results(target, start_port, end_port)
    print("Scan results saved to scan_results.txt.")
import socket
import threading
import logging
from datetime import datetime
import os

logging.basicConfig(filename="port_scanner.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port} is OPEN")
            logging.info(f"Port {port} is OPEN on {target}")
        
        sock.close()
    except socket.timeout:
        logging.warning(f"Timeout error on port {port} for {target}")
    except Exception as e:
        logging.error(f"Error on port {port}: {e}")

def port_scanner(target, start_port, end_port):
    print(f"\nStarting scan on target: {target}")
    print(f"Scanning ports from {start_port} to {end_port}...\n")

    threads = []
    
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def save_results(target, start_port, end_port):
    with open("scan_results.txt", "w") as file:
        file.write(f"Port scan results for {target} from port {start_port} to {end_port}\n")
        file.write("="*50 + "\n")
        with open("port_scanner.log", "r") as log_file:
            file.write(log_file.read())

if __name__ == "__main__":
    print("Welcome to the Advanced Python Port Scanner")
    
    target = input("Enter the target (IP or hostname): ")
    while True:
        try:
            start_port = int(input("Enter the start port: "))
            end_port = int(input("Enter the end port: "))
            if start_port < 1 or end_port > 65535 or start_port > end_port:
                raise ValueError
            break
        except ValueError:
            print("Please enter valid port numbers between 1 and 65535, with the start port less than or equal to the end port.")
    
    start_time = datetime.now()

    port_scanner(target, start_port, end_port)

    end_time = datetime.now()
    print(f"\nScan completed in: {end_time - start_time}")

    save_results(target, start_port, end_port)
    print("Scan results saved to scan_results.txt.")
