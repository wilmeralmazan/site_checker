#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
server_status_checker.py

Author: Wilmer Almazan
Email: wilmeralmazan@gmail.com
Date Created: November 14, 2023
Last Modified: November 14, 2023
Version: 1.0
Description:
    This script checks whether a specified web server is online by attempting to
    establish a socket connection using a provided host and port. It sends a
    simple HTTP HEAD request and checks the server's response.

"""

import sys
import socket

# Check if the correct number of arguments are provided
if len(sys.argv) not in [2, 3]:
    print("Usage: script.py <host> [port]")
else:
    try:
        host = sys.argv[1]
        # Use a default port if not specified, otherwise convert to integer
        port = 80 if len(sys.argv) == 2 else int(sys.argv[2])
        
        print(f"Attempting to connect to {host} on port {port}")

        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        sock.connect((host, port))

        # Send a simple HTTP HEAD request
        request = f"HEAD / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
        sock.send(request.encode('utf-8'))

        # Receive the response
        reply = sock.recv(10000)
        print("Server Online")

        # Properly shutdown and close the socket
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()

    except ValueError:
        print("Port must be an integer.")
    except socket.gaierror:
        print("Hostname could not be resolved.")
    except socket.error as e:
        print(f"Server Down - Socket Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")