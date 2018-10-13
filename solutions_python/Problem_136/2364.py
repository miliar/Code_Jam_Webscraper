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

fdata=DataFromFile("cookie.in")
fname="cookie.out"
with open(fname, "w") as f:
	pass
#
lines=fdata.split("\n")
lines.pop()
cases=int(NextLine())
for k1 in xrange(cases):
	tprev=1e100
	tmp=map(float, (NextLine()).split(" "))
	#print tmp
	vC=tmp[0]  #Cost per farm.
	vF=tmp[1]  #Cookie creation rate per farm.
	vX=tmp[2]  #Final required balance.
	t=0
	farm=0
	donext=1
	while (donext==1):
		rate=2+vF*farm
		ttBuy=vC/rate
		ttFinal=t+vX/rate
		if (ttFinal<tprev):
			tprev=ttFinal
			donext=1
		else:
			donext=0
		#
		#print "t="+str(t)+"   farm="+str(farm)+"   ttBuy="+str(ttBuy)+"   ttFinal="+str(ttFinal)+" "+str(donext)
		t=t+ttBuy
		farm=farm+1
	#
	tmps="Case #"+str(k1+1)+": "+str(tprev)
	#print tmps
	TxtAppend(fname,tmps)
# end of each case
