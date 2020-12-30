# Importing Required Modules
import socket as s
import threading as thd
import os

# Create a Socket and Bind IP and PORT to It
skt = s.socket(s.AF_INET, s.SOCK_DGRAM)
localIP = input("Enter Your IP: ")
skt.bind((localIP, 8081))

# Get Partner's IP to chat with
usrIP = input("Enter Partner's IP: ")
print()

# Function to Send the Message
def send_msg():
    while True:
        data = input()
        if data == "quit":
            break
        msgSent = skt.sendto(data.encode(), (usrIP, 8081))


# Calling the Send Message Function
send_msg()
