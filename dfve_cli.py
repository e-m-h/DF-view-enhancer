import binascii
import re
import shutil


#modifying SAVETREE.DAT

# Taken from https://en.uesp.net/dagger/daghack.shtml#moreview
#0x7F	29	(50m)	0%	Bethesda's max choice, smooth everywere
#0x9F	33	(57m)	14%	smooth limit on big towns borders
#0xCF	39	(67m)	34%	rough on big towns borders, smooth limit in outlands
#0xD7	40	(69m)	38%	a little rough in outlands, smooth in towns
#0xDF	41	(71m)	41%	rough in outlands, smooth limit in towns
#0xEF	42	(72m)	45%	rough in towns at view sides, smooth at center
#0xFF	42	(72m)	45%	max value, rough nearly everywhere.

#dis = 'ff7f0080'

# Meat & Potatoes
def makeBackup():
	shutil.copyfile('SAVETREE.DAT','SAVETREE.BKP')

def distanceChange():
	with open('SAVETREE.DAT', 'rb') as f, open('newsavetree', 'wb') as fout:
		hexdata = binascii.hexlify(f.read())
		stuff = (hexdata.decode())
		stuff = re.sub(r'7f7f0080', dis, stuff)
		stuff = stuff.encode()
		fout.write(
			binascii.unhexlify(stuff)
		)

print("List of view distance options:\n\
1) 14% - Smooth limit on big town borders\n\
2) 34% - Rough on big town borders, smooth limit in wilderness\n\
3) 38% - A little rough in wilderness, smooth in towns\n\
4) 41% - Rough in wilderness, smooth in towns\n\
5) 45% - Rough in towns at view sides, smooth at center\n\
6) 45% - Max value, rough nearly everywhere\n")
# This is ugly. Look into using a dictionary
sel = input("Which view distance would you prefer? ")
if sel == '1':
	dis = '9f7f0080'
elif sel == '2': 
	dis = 'cf7f0080'
elif sel == '3':
    dis = 'd77f0080'
elif sel == '4':
    dis = 'df7f0080'
elif sel == '5':
    dis = 'ef7f0080'
elif sel == '6':
    dis = 'ff7f0080'


#print(dis)
distanceChange()
