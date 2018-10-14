#!/opt/local/bin/python2.7
import sys
import io
import math

#if numstr is fair, return 1. else,return 0.
def isfair(numstr):
	if(numstr != 1):
		ispalin=1
		for i in range(0,int(math.ceil(len(numstr)/2.0))):
			if(numstr[i] != numstr[len(numstr)-1-i]):
				ispalin=0
				break;
		return ispalin
	else:
		return 1

def check(mins,maxs):

	minsqrt=int(math.floor(math.sqrt(int(mins))) )
	maxsqrt=int(math.floor(math.sqrt(int(maxs))) )
	count=0
	if(minsqrt*minsqrt != int(mins)):
		minsqrt=minsqrt+1
	while (minsqrt <= maxsqrt):
		if(isfair(str(minsqrt)) == 1 and isfair(str(minsqrt*minsqrt)) == 1):
			print minsqrt
			count = count + 1;
		minsqrt=minsqrt+1
	return count

	
if(len(sys.argv) != 2):
	exit(1)
inp=open(sys.argv[1],'r')
outp=open("out.txt",'w')
casecount = int(inp.readline())
print casecount
testcount = 0
while(testcount < casecount):
	result = 0;#0 NO 1 X YES
	testcount=testcount+1
	minmaxlist = inp.readline()
	minmaxlist = minmaxlist.split(' ')
	print minmaxlist
	print "Case #"+str(testcount)+": "+str(check(minmaxlist[0],minmaxlist[1]))
	outp.write("Case #"+str(testcount)+": "+str(check(minmaxlist[0],minmaxlist[1]))+"\n")

exit(0)
