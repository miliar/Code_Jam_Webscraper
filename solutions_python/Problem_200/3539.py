import sys

T = None
cases = []
with open(sys.argv[1]) as f:
	T = int(f.readline())
	for l in f.readlines():
		cases.append([int(x) for x in l.strip()])

def dec(n,c):
	flag = False
	for j in range(len(n)):
		if not flag:
			if n[j]<c:
				continue
			if n[j]==c:
				n[j] = c -1
				flag = True
		else:
			n[j] = 9
def printCase(i,n):
	print "Case #{}: {}".format(i,''.join([str(x) for x in n]).lstrip('0'))

for I,C in enumerate(cases):
	if len(C) == 1:
		printCase(I+1,C)
		continue
	for d in range(1,len(C)):
		#print d,C
		if C[d] < C[d-1]:
			dec(C,C[d-1])
			#print C
	printCase(I+1,C)