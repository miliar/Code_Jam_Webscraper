import re
import sys
sys.stdin = open("input.test","r")
sys.stdout = open("output.test","w")
line = raw_input().split()
l,d,n = int(line[0]),int(line[1]),int(line[2])
dt = {}
pt = {}
# get the words
for i in range(d):
	dt[i] = raw_input()
# now we got the words
# get the patterns
for i in range(n):
	pt[i] = raw_input().replace("(","[").replace(")","]")
# got them too
for i in pt:#for each pattern
	num = 0
	for j in dt:
		#print "Matching",dt[j],"with",pt[i]
		if re.match(pt[i],dt[j]) != None:
			num+=1
	print "Case #%d: %d\n" % (i+1,num),
#raw_input()
sys.stdout.close()
