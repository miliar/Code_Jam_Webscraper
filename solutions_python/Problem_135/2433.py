import os

def DataFromFile(fname):
	with open(fname,"r") as f:
		tline=f.read()
	return tline
#
def TxtAppend(fname,s):
	with open(fname, "a") as f:
		f.write(s+"\n")
#
lnum=0
def NextLine():
	global lnum
	lnum=lnum+1
	return lines[lnum-1]
#

fdata=DataFromFile("magic.in")
fname="magic.out"
with open(fname, "w") as f:
	pass
#
lines=fdata.split("\n")
lines.pop()
cases=int(NextLine())
for k1 in xrange(cases):
	row1=int(NextLine())
	ccount=[0]*16
	for k2 in xrange(4):
		crow=NextLine().split(" ")
		if (k2==(row1-1)):
			for k3 in map(int, crow):
				ccount[k3-1]=ccount[k3-1]+1
			#
		#
	#
	row2=int(NextLine())
	for k2 in xrange(4):
		crow=NextLine().split(" ")
		if (k2==(row2-1)):
			for k3 in map(int, crow):
				ccount[k3-1]=ccount[k3-1]+1
			#
		#
	#
	count2=0
	find2=0
	for k2 in xrange(16):
		if (ccount[k2]==2):
			count2=count2+1
			find2=k2
		#
	#
	if (count2==1):
		TxtAppend(fname,"Case #"+str(k1+1)+": "+str(find2+1))
	elif (count2==0):
		TxtAppend(fname,"Case #"+str(k1+1)+": Volunteer cheated!")
	elif (count2>1):
		TxtAppend(fname,"Case #"+str(k1+1)+": Bad magician!")
	#
#
