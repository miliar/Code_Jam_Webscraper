#!/opt/local/bin/python2.7
import sys
import math
import io

def check(rad,ink):
	rad=rad+1
	count=1
	square = 2*rad-1
	while(square <= ink):
		ink = ink - square
		rad = rad+2
		square = 2*rad-1
		count=count+1
		
		
	return count-1
	
if(len(sys.argv) != 2):
	exit(1)
inp=open(sys.argv[1],'r')
outp=open("out.txt",'w')
casecount = int(inp.readline())
print casecount
testcount = 0
while(testcount < casecount):
	testcount=testcount+1
	data = inp.readline()
	datalist = data.split(' ')
	
	print "Case #"+str(testcount)+": "+str(check(int(datalist[0]),int(datalist[1])))
	outp.write("Case #"+str(testcount)+": "+str(check(int(datalist[0]),int(datalist[1])))+"\n")

exit(0)
