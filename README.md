# Server Status Checker

## Overview
This Python script, `site_checker.py`, is designed to quickly check the status of a web server. It attempts to establish a socket connection to a specified host and port and sends a simple HTTP HEAD request to determine if the server is online.

## Features
- Simple and easy-to-use command-line interface.
- Ability to specify the host and port.
- Default port is 80 if not specified.
- Provides clear status output about the server's availability.

## Prerequisites
Ensure you have Python installed on your system. This script is compatible with Python 3.x.

## Installation
Clone this repository to your local machine to get started.

git clone https://github.com/wilmeralmazan/site_checker.git

cd site_checker

pip install -e .

## Usage
Run the script from the command line by passing the host and an optional port number.
Usage: check_site [OPTIONS]

Options:
  -h, --host TEXT     Domain name or IPv4 address  [required]
  -p, --port INTEGER  Port number  [default: 80]
  --help              Show this message and exit.

### Example
check_site --hostname devnetjourney.com --port 80

## Error Handling
The script includes error handling for common issues such as:
- Incorrect argument format.
- Non-integer port numbers.
- Unresolvable hostnames.
- Socket connection errors.

## Contributions
Contributions to this project are welcome! Please fork the repository and submit a pull request with your enhancements.

## License
This project is licensed under the [MIT License](LICENSE).

