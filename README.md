# X3-PORTFINDER - Port Scanner

![X3-PORTFINDER Banner](banner.gif)

X3-PORTFINDER is a powerful, lightweight, and user-friendly port scanning tool developed by X3NIDE. It's designed to provide quick and detailed insights into open ports on target systems, with a focus on potential vulnerabilities.

## Features

- **Sleek Neon Cyan Interface**: Enjoy a visually appealing and professional command-line interface.
- **Multi-threaded Scanning**: Fast and efficient scanning using concurrent connections.
- **Detailed Vulnerability Information**: Get instant insights into potential vulnerabilities for each open port.
- **Real-time Progress Tracking**: Stay informed with a dynamic progress bar during scans.
- **Custom Port Range**: Specify your desired port range for targeted scanning.
- **User-friendly Output**: Clear and concise presentation of scan results.

## What Makes X3-PORTFINDER Unique

1. **Aesthetic Appeal**: Unlike traditional port scanners with plain text output, X3-PORTFINDER features a sleek neon cyan interface that's easy on the eyes and professional in appearance.

2. **Instant Vulnerability Insights**: While most scanners only identify open ports, X3-PORTFINDER provides immediate information about potential vulnerabilities associated with each discovered service.

3. **Efficient and Informative**: The tool strikes a perfect balance between speed (using multi-threading) and information density, providing valuable insights without overwhelming the user.

4. **Developer-friendly Code**: The source code is extensively commented, making it easy for other developers to understand, modify, or contribute to the project.

5. **Focused Scope**: X3-PORTFINDER is designed to do one thing exceptionally well - port scanning with vulnerability hints. It's not bloated with unnecessary features, ensuring simplicity and efficiency.

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/mubbashirulislam/X3-portfinder.git
   ```

2. Navigate to the project directory:
   ```
   cd X3-portfinder
   ```

3. (Optional) Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

## Usage

Run X3-PORTFINDER using the following command:

```
python x3port.py <target> [start_port] [end_port]
```

- `<target>`: The IP address or hostname to scan (required)
- `[start_port]`: The first port to scan (optional, default is 1)
- `[end_port]`: The last port to scan (optional, default is 1024)

### Examples

Scan all ports from 1 to 1024 on example.com:
```
python x3port.py example.com
```

Scan ports 80 to 443 on 192.168.1.1:
```
python x3port.py 192.168.1.1 80 443
```

## Contributing

Contributions to X3-PORTFINDER are welcome! Please feel free to submit pull requests, create issues or spread the word.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

X3-PORTFINDER is designed for educational and ethical testing purposes only. Always ensure you have explicit permission to scan any systems or networks that you do not own or operate. Unauthorized port scanning may be illegal in some jurisdictions.

## Contact

For questions, suggestions, or collaborations, please open an issue on this GitHub repository or contact X3NIDE directly via GitHub.
