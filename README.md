# NibbleBlog-Brute-Force
This is a simple brute force attack tool to use against NibbleBlog, it is specialized in bypassing the Blacklist Protection of NibbleBlog via X-Forwarded-For HTTP Header.

usage: nibbleblog-brute-force.py [-h] [--username USERNAME] [--wordlist WORDLIST] [--network NETWORK] [--url URL]

Simple NibbleBlog Brute Force Attack Tool

optional arguments:
  -h, --help           show this help message and exit
  --username USERNAME  This option is to specify the target username
  --wordlist WORDLIST  This option is to specify the path to the passwords wordlist
  --network NETWORK    This option is to specify the network (EX: 192.168.1.0/24) to spoof the source IP addresses
  --url URL            This option is to specify the target URL with the admin.php uncluded

if you want to contribute please contact me at rafaelonieltrinidadpolanco@gmail.com
