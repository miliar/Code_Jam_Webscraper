import math
def solve(l1,caseNum):
	n,m = map(int,l1.split())
	
	start = int(math.ceil(math.sqrt(n)))
	end = int(math.sqrt(m))
	s = [x for x in range(start,end+1) if isPol(x)]
	y = [x for x in s if isPol(x**2)]

	o.write('Case #'+ str(caseNum) + ': ' + str(len(y)) + '\n')
	print 'Case #'+ str(caseNum) + ': ' + str(len(y))
	
def isPol(x):
	x = str(x)
	for i in range((len(x)/2)+1):
		if x[i] != x[-(i+1)]:
			return False

	return True

f = open('input.in', 'r')

o = open('out.txt','w')
lines = f.read().splitlines()
cases = int(lines[0])
for i in range(1,cases+1):
	solve(lines[i],i)
f.close()
o.close()