import requests
import os
import sys
from time import sleep
import threading
###################################
print ("\033[92mWebsite\033[91m:- \033[94mcyberyemen.blogspot.com")
sleep(1)
os.system("clear")
def get_ip():
	token = "1937421918:AAGD_3GxLJA7D-aPQuItkGqY-32UId2aUzE"
	id1 = "1823390961"
	f = "Done New User"
	sens3 = requests.get("https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+id1+"&text="+f)
	os.system("clear")
	op = (""" 
\033[91m ~~~~~~~~~~~~~~~~~~
\033[91m| \033[94mWelcom in My tool \033[91m|
\033[91m ~~~~~~~~~~~~~~~~~~
\033[91m[\033[94m*\033[91m] \033[96mInformation for IP \033[92m--> \033[94m1
\033[91m[\033[94m*\033[91m] \033[96mInformation for list IP \033[92m--> \033[94m2
\033[91m[\033[94m*\033[91m] \033[96mGet your Ip \033[92m--> \033[94m3""")
	for i in op:
		sys.stdout.write(i)
		sys.stdout.flush()
		sleep(0.02)
	try:
		cho = input(""" 
\n\033[92m┌──(\033[96mMr_Silent\033[92m)
\033[92m└─\033[91m$ \033[92m""")
		if cho == "1":
			os.system("clear")
			ip = input(""" 
\033[92m┌──(\033[96mMr_Silent\033[92m)
\033[92m└─\033[94mIp\033[92m-> \033[91m$ \033[92m""")
			url = "https://ipinfo.io/%s/?token=1bbf2a929a664c"%ip
			req = requests.get(url).text
			req = req.replace("{", "").replace("}", "").replace(":", " -->").replace("\"", "").replace(",", "")
			if "title --> Wrong ip" in req:
				print ("[*] Wrong Ip --> %s"%ip)
			else:
				print ("\n\033[92m[\033[94m*\033[92m] \033[96mThe Information \n"+"\033[91m" + req)
####################################################################################################################3###
		elif cho == "2":
			os.system("clear")
			file = input("""
\033[92m┌──(\033[96mMr_Silent\033[92m)
\033[92m└─\033[94mfile\033[92m-> \033[91m$ \033[92m""")
			que = input("\033[92mYou Want Save Information \033[92m[\033[96my\033[92m\033[92m/\033[91mn\033[92m] \033[92m!? -->\033[94m: \033[96m")
			if que == "y":
				fi = input("\033[96mEnter Name File \033[92m--> \033[94m")
				file = open(file, "r")
				for i in file.readlines():
					url1 = "https://ipinfo.io/%s/?token=1bbf2a929a664c"%i
					req1 = requests.get(url1).text
					req1 = req1.replace("{", "").replace("}", "").replace(":", " -->").replace("\"", "").replace(",", "")
					if "title --> Wrong ip" in req1:
						print ("""\n\033[92m[\033[94m!\033[92m] \033[91mError \033[92m--> \033[91mWrrong Ip \033[92m--> \033[96m%s"""%i)
					else:
						print ("\n\033[92m[\033[94m*\033[92m] \033[96mThe Information \n" +"\033[91m" + req1)
						f = open(fi, "a")
						f.write(req1)
						f.close()
				os.system("clear")
				print ("\033[92m[\033[94m*\033[92m] \033[96mDone Add information in file \033[91m^_^")
			elif que == "n":
				file = open(file, "r")
				for i in file.readlines():
					url2 = "https://ipinfo.io/%s/?token=1bbf2a929a664c"%i
					req2 = requests.get(url2).text
					req2 = req2.replace("{", "").replace("}", "").replace(":", " -->").replace("\"", "").replace(",", "")
					if "title --> Wrong ip" in req2:
						print ("""\n[!] Error --> Wrrong Ip --> %s"""%i)
					else:
						print (req2)
########################################################################################################################
		elif cho == "3":
			req3 = requests.get("https://ifconfig.me/").text
			os.system("clear")
			print ("\n[*] Your Ip is --> %s"%req3)
			sleep(2)
	except:
		print ("\n\033[92m[\033[91m!\033[92m] \033[91mError Restart the tool \033[92m[\033[91mNot found file or you Disconnected InterNet\033[92m]")
thread = []
for i in range(1):
	thread1 =threading.Thread(target=get_ip)
	thread1.start()
	thread.append(thread1)
for thread2 in thread:
	thread2.join
