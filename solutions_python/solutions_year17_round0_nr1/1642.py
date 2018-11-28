import sys
import bisect

inputfile = open(sys.argv[1])
lines = inputfile.readlines()
testcases = int(lines[0].split()[0])
testcase=0

def flip(l):
	for i in xrange(len(l)):
		if l[i]=='+':
			l[i]='-'
		else:
			l[i]='+'
	return l

for line in lines[1:]:
	testcase+=1
	test=list(line.split()[0])
	k=int(line.split()[1])
	i=0
	res=0
	flag = True
	while(i<len(test)):
		if test[i]=='-':
			if ((i+k)>len(test)):
				flag=False
				break
			else:
				test[i:i+k]=flip(test[i:i+k])
				res+=1
		i+=1
	if flag:
		print("Case #%d: %d"%(testcase,res))
	else:
		print("Case #%d: IMPOSSIBLE"%(testcase))

