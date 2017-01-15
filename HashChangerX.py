from Tkinter import *
import tkFileDialog
import os
import hashlib





def myFunc():
	dir_opt = {}
	#dir_opt['initialdir'] = os.environ["HOME"] + '\\'
	dir_opt['mustexist'] = False
	#dir_opt['parent'] = self
	dir_opt['title'] = 'Please select directory'
	result = tkFileDialog.askdirectory()

	changeName(result)
	#self.changeHash(result)




def changeName(path):
	for filename in os.listdir(path):
		fullpath = path + "/" + filename
		if os.path.isfile(fullpath):

			#no hidden files like .DS_Store
			if filename[0] != "." :

				#do not affect the file itself
				if filename != __file__:

					#chane hash
					changeHash(fullpath)

					extension = filename.split(".")[-1]		
					newName = hashlib.md5(filename.encode()).hexdigest()

					if var1.get():
						os.rename(fullpath, path + "/" + newName + "." + extension)



				

def changeHash(path):
	if var2.get():
		file = open(path, "rb")
		data = file.read()
		file.close()

		data += '\0'

		output = open(path, "wb")
		output.write(data)
		output.close()






master = Tk()

Label(master, text="Actions:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="rename", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="rehash", variable=var2).grid(row=2, sticky=W)

Button(master, text='Open Folder', command=myFunc).grid(row=4, sticky=W, pady=4)
mainloop()
