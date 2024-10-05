# Import necessary modules
import sys  # For command-line arguments and system-specific parameters
import socket  # For network operations
from datetime import datetime  # For timestamps
import concurrent.futures  # For multi-threading

# Define ANSI color codes for terminal output
NEON_CYAN = "\033[96m"  # Neon cyan color
RED = "\033[91m"  # Red color for warnings and open ports
BOLD = "\033[1m"  # Bold text
RESET = "\033[0m"  # Reset all text attributes

# Dictionary of common ports with their services and potential vulnerabilities
PORT_DETAILS = {
    20: ("FTP Data", "Unauthorized access, data theft"),
    21: ("FTP Control", "Brute-force attacks, anonymous access"),
    22: ("SSH", "Brute-force attacks, outdated SSH exploits"),
    23: ("Telnet", "Clear-text transmission, MITM attacks"),
    25: ("SMTP", "Open relay, email spoofing, spamming"),
    53: ("DNS", "DNS amplification, cache poisoning"),
    80: ("HTTP", "Web app vulnerabilities, XSS, SQL injection"),
    110: ("POP3", "Clear-text emails, credential attacks"),
    143: ("IMAP", "Clear-text emails, IMAP vulnerabilities"),
    443: ("HTTPS", "SSL/TLS misconfigurations, outdated ciphers"),
    3306: ("MySQL", "SQL injection, unauthorized db access"),
    3389: ("RDP", "BlueKeep, brute-force, session hijacking"),
}

def print_banner():
    """
    Print the ASCII art banner for X3-PORTFINDER with developer information.
    """
    banner = """
██╗  ██╗██████╗       ██████╗  ██████╗ ██████╗ ████████╗███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
╚██╗██╔╝╚════██╗      ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
 ╚███╔╝  █████╔╝█████╗██████╔╝██║   ██║██████╔╝   ██║   █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
 ██╔██╗  ╚═══██╗╚════╝██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
██╔╝ ██╗██████╔╝      ██║     ╚██████╔╝██║  ██║   ██║   ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚═════╝       ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                        Developed by X3NIDE
                                https://github.com/mubbashirulislam
    """
    print(f"{NEON_CYAN}{BOLD}{banner}{RESET}")  # Print the banner in neon cyan and bold

def print_header(text):
    """
    Print a header with the given text.
    
    Args:
    text (str): The header text to be printed.
    """
    print(f"\n{NEON_CYAN}{BOLD}{text}{RESET}")  # Print the header text in neon cyan and bold
    print(f"{NEON_CYAN}{'-' * 60}{RESET}")  # Print a line under the header

def print_info(label, value):
    """
    Print an information line with a label and value.
    
    Args:
    label (str): The label for the information.
    value (str): The value of the information.
    """
    print(f"{NEON_CYAN}{BOLD}{label}:{RESET} {value}")  # Print label in neon cyan and bold, value in default color

def print_port_info(port, service, vulnerability):
    """
    Print information about an open port.
    
    Args:
    port (int): The port number.
    service (str): The service running on the port.
    vulnerability (str): Potential vulnerabilities associated with the port.
    """
    print(f"\n{RED}{BOLD}Port {port} - {service}{RESET}")  # Print port and service in red and bold
    print(f"{NEON_CYAN}Potential Vulnerability:{RESET} {vulnerability}")  # Print vulnerability info

def scan_port(target, port):
    """
    Attempt to connect to a specific port on the target.
    
    Args:
    target (str): The IP address or hostname to scan.
    port (int): The port number to scan.
    
    Returns:
    int or None: The port number if open, None if closed.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # Create a new socket
            s.settimeout(1)  # Set a 1-second timeout for the connection attempt
            result = s.connect_ex((target, port))  # Attempt to connect to the port
            if result == 0:  # If connection successful, port is open
                return port
    except:
        pass  # If any error occurs, assume the port is closed
    return None

def get_port_details(port):
    """
    Get the service name and vulnerability information for a given port.
    
    Args:
    port (int): The port number to look up.
    
    Returns:
    tuple: A tuple containing the service name and vulnerability information.
    """
    return PORT_DETAILS.get(port, ("Unknown", "Investigate non-standard service"))  # Return details or default message

def main(target, start_port=1, end_port=1024, threads=100):
    """
    Main function to run the port scanner.
    
    Args:
    target (str): The target IP address or hostname.
    start_port (int): The first port to scan (default: 1).
    end_port (int): The last port to scan (default: 1024).
    threads (int): Number of concurrent threads to use (default: 100).
    """
    try:
        target = socket.gethostbyname(target)  # Resolve hostname to IP address
        
        print_banner()  # Print the X3-PORTFINDER banner

        print_header("Scan Information")  # Print scan information header
        print_info("Target", target)  # Display target IP
        print_info("Port Range", f"{start_port}-{end_port}")  # Display port range
        print_info("Scan Started", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # Display start time

        open_ports = []  # List to store open ports

        # Use ThreadPoolExecutor for concurrent port scanning
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            # Create a future for each port scan
            futures = [executor.submit(scan_port, target, port) for port in range(start_port, end_port + 1)]
            for i, future in enumerate(concurrent.futures.as_completed(futures)):
                result = future.result()
                if result:
                    open_ports.append(result)  # Add open port to the list
                # Update progress bar
                progress = (i + 1) / (end_port - start_port + 1) * 100
                sys.stdout.write(f"\r{NEON_CYAN}Scanning: [{'=' * int(progress / 2):<50}] {progress:.1f}%{RESET}")
                sys.stdout.flush()

        print("\n")  # Print newline after progress bar
        if open_ports:
            print_header("Scan Results")  # Print results header
            for port in sorted(open_ports):
                service, vulnerability = get_port_details(port)  # Get port details
                print_port_info(port, service, vulnerability)  # Print information for each open port
        else:
            print_header("No Open Ports Found")  # Inform if no open ports were found

        print(f"\n{NEON_CYAN}Scan Completed: {RESET}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")  # Print completion time

    except KeyboardInterrupt:
        print(f"\n{RED}Scan interrupted by user.{RESET}")  # Handle user interruption
    except socket.gaierror:
        print(f"{RED}Error: Hostname could not be resolved.{RESET}")  # Handle hostname resolution error
    except socket.error:
        print(f"{RED}Error: Could not connect to server.{RESET}")  # Handle connection error

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Print usage instructions if insufficient arguments are provided
        print(f"{RED}Usage: python3 x3_portfinder.py <target> [start_port] [end_port]{RESET}")
        sys.exit(1)

    target = sys.argv[1]  # Get target from command line arguments
    start_port = int(sys.argv[2]) if len(sys.argv) > 2 else 1  # Get start port or use default
    end_port = int(sys.argv[3]) if len(sys.argv) > 3 else 1024  # Get end port or use default

    # Validate port range
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print(f"{RED}Error: Invalid port range. Use ports between 1 and 65535.{RESET}")
        sys.exit(1)

    main(target, start_port, end_port)  # Run the main scanning function