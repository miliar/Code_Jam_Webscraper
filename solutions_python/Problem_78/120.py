inf = open("in.txt","r")
ouf = open("out.txt","w")

def precalc():
	pass
	
testnum=0
def writestring(s):
	global testnum
	testnum+=1
	s="Case #"+str(testnum)+": "+s
#	print <ouf, s
	print s

def solvetest():
	a=inf.readline().split()
	a=a[1:]
	who=1
	whb=1
	zo=0
	zb=0
	res=0
	for i in xrange(len(a)/2):
		col=a[2*i]
		num=int(a[2*i+1])
		if col=='O' :
			res+=max(0,abs(num-who)-zo)+1
			zb+=max(0,abs(num-who)-zo)+1
			zo=0
			who=num
		else:
			res+=max(0,abs(num-whb)-zb)+1
			zo+=max(0,abs(num-whb)-zb)+1
			zb=0
			whb=num
	writestring(str(res))

precalc()
counttests=int(inf.readline())
for i in xrange(counttests):
	solvetest()
