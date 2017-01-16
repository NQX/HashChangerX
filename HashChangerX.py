from Tkinter import *
import tkFileDialog
import os
import hashlib
from PIL import Image



path = None
fullpath = None
#result = None


def selectFolder():
	global path
	dir_opt = {}
	#dir_opt['initialdir'] = os.environ['USERPROFILE'] 
	dir_opt['initialdir'] = os.path.expanduser('~')
	dir_opt['mustexist'] = False
	#dir_opt['parent'] = self
	dir_opt['title'] = 'Please select directory'
	path = tkFileDialog.askdirectory()
	statusText.set("Folder selected: " + path)
	
	#self.changeHash(result)




def changeName(path, filename):
	statusText.set("Done")

	print("path " + path)
	print("filename " + filename)
							

	fileNameWithoutExtension = filename.split(".")[0]

	newName = hashlib.md5(fileNameWithoutExtension.encode()).hexdigest()
	extension = getExtension(filename)

	os.rename(path + "/" + filename, path + "/" + newName + "." + extension)



				

def changeHash(path):
	print("old md5: " + hashlib.md5(open(path, 'rb').read()).hexdigest())

	file = open(path, "rb")
	data = file.read()
	file.close()

	data += '\0'

	output = open(path, "wb")
	output.write(data)
	output.close()
	print("new md5: " + hashlib.md5(open(path, 'rb').read()).hexdigest())



def convertPngToJpg(path, filename):
	#print("Old type " + path)
	fullpath = path + "/" + filename
	im = Image.open(fullpath)
	pathWithoutExtension = fullpath.split(".")[0]

	im.save(pathWithoutExtension + ".jpg", "JPEG")
	os.remove(fullpath)

	fileNameWithoutExtension = filename.split(".")[0]
	return fileNameWithoutExtension + ".jpg"






def checkIfValid(file):
	global path
	
	if os.path.isfile(path + "/" + file) and file[0] != "." and file != __file__ : 
		#no hidden files like .DS_Store
		#do not affect the file itself
			
		return True
	else :
		return False






def isPng(ext):
	if ext.lower() == "png":
		return True
	else:
		return False


def getExtension(path):
	ext = path.split(".")[-1]

	return ext



def start():
	global path
	
	if path:
		for filename in os.listdir(path):
			print("filename " + filename)
			fullpath = path + "/" + filename
			extension = getExtension(fullpath)
			if checkIfValid(filename):
				
				if var2.get():
					changeHash(fullpath)

				if var3.get() and isPng(extension):
					filename = convertPngToJpg(path, filename)
					fullpath = path + "/" + filename
			
				if var1.get():
					changeName(path, filename)





master = Tk()

master.title("HashChangerX")
master.resizable(0, 0)
master.minsize(200, 200)


Label(master, text="Actions:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="rename", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="rehash", variable=var2).grid(row=2, sticky=W)
var3 = IntVar()
Checkbutton(master, text="Png to Jpg", variable=var3).grid(row=3, sticky=W)

statusText = StringVar()
Label(master, textvariable=statusText).grid(row=4, sticky=W)
statusText.set("Ready")

Button(master, text='Open Folder', command=selectFolder).grid(row=5, sticky=W, pady=4)
Button(master, text='Start', command=start).grid(row=6, sticky=W)
mainloop()
