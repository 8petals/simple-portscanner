
import socket
import termcolor
import pyfiglet

banner = pyfiglet.figlet_format("8petals", font = "banner")
print(banner)

count = 0

def scan(target, ports):
	print(termcolor.colored(('\n' + 'Starting Scan For ' + str(target)), 'blue'))
	for port in range(1,ports):
		scan_port(target, port)

def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Port Opened " + str(port))
		sock.close
		count = count+1
	except:
		pass

targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

if ',' in targets:
	print(termcolor.colored(("[*] Scanning for Multiple Targets"), 'blue'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets, ports)

if count>0:
	print('\n',termcolor.colored(("[*] Found ",count," Ports Opened in the Target List"), 'green'))
else:
	print('\n',termcolor.colored(("[*] No Opened Port Found in the Target List"), 'red'))
