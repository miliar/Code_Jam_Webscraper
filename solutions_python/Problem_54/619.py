import math
def amcd(a):
	d=range(0,len(a)-1,1)
	i=0
	for i in range(0,len(a)-1,1):
		d[i]=a[i+1]-a[i]	
	if len(d):
		ret=d[0]
	else:
		ret=a[0]	
	for i in range(1,len(d),1):
		ret=mcd(ret,d[i])	
	return ret
	
def mcd(a,b):
	if b == 0:
		return a
	while ((a%b)!=0):
		c=b
		b=a%b
		a=c
 	return b
def testcase(a):
	nMcd=amcd(a)	
	if nMcd == 0:
		return 0
	ret=long(math.ceil(float(a[0])/float(nMcd))*nMcd)-a[0]
	if ret<0:
		return nMcd+ret
	else:
		return ret
lines=open("B-small-attempt1.in","r")
nT=lines.readline()
iT=0
for line in lines:
	iT=iT+1
	line=line.strip()
	lineData=line.split(" ",1)		
	nEvents=lineData[0] 
	aEventsTimeAgo=lineData[1].split(" ")	
	for s in range(0,len(aEventsTimeAgo),1):
		aEventsTimeAgo[s]=long(aEventsTimeAgo[s])
	aEventsTimeAgo.sort()
	print "Case #"+str(iT)+": "+str(testcase(aEventsTimeAgo))


