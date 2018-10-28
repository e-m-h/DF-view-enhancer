import binascii
import re
import shutil
from tkinter import *


#modifying SAVETREE.DAT
#00009b20
#Offset is 9B29

# Taken from https://en.uesp.net/dagger/daghack.shtml#moreview
#0x7F	29	(50m)	0%	Bethesda's max choice, smooth everywere
#0x9F	33	(57m)	14%	smooth limit on big towns borders
#0xCF	39	(67m)	34%	rough on big towns borders, smooth limit in outlands
#0xD7	40	(69m)	38%	a little rough in outlands, smooth in towns
#0xDF	41	(71m)	41%	rough in outlands, smooth limit in towns
#0xEF	42	(72m)	45%	rough in towns at view sides, smooth at center
#0xFF	42	(72m)	45%	max value, rough nearly everywhere.


class Window(Frame):

	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.master = master

root = Tk()
app = Window(root)
###
#window = Tk()

#window.title( 'Daggerfall View Enhancer')
#label = Label(window, text = 'Where Things Go')
#label.pack(padx = 200, pady = 50)


# Window things
def tog():
	if root.cget('bg') == 'yellow':
		root.configure(bg = 'gray')
	else:
		root.configure(bg = 'yellow')

# Meat & Potatoes
def makeBackup():
	shutil.copyfile('SAVETREE.DAT','SAVETREE.BKP')

def changeDistance():
	with open('SAVETREE.DAT', 'rb') as f, open('newsavetree', 'wb') as fout:
		hexdata = binascii.hexlify(f.read())
		stuff = (hexdata.decode())
		stuff = re.sub(r'7f7f0080', 'ff7f0080', stuff)
		stuff = stuff.encode()
		fout.write(
			binascii.unhexlify(stuff)
		)



btn_mkBkp = Button(root, text = "Make backup", command=makeBackup)
btn_end = Button(root, text = 'Close', command=exit)

btn_mkBkp.pack(padx = 150, pady = 20)
btn_end.pack(padx = 150, pady = 20)

root.mainloop()
#changeDistance()
