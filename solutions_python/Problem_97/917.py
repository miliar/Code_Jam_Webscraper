import sys

def perm(x,a,b):
	x = str(x)
	tmp = []
	for i in range(len(x)):
		tmp.append(int(x[i:]+x[:i]))
	return set([i for i in tmp if i<int(x) and i>=a and i<=b])

f = open(sys.argv[1],"r")

T = int(f.readline())

for c in range(T):
	l = map(int,f.readline().split())
	a = l[0]
	b = l[1]
	count = 0
	tmp = []
	for i in range(a,b+1):
		#print i, [j for j in perm(i) if j!=i and j>=a and j<=b]
		count += len(perm(i,a,b))
	print "Case #" + str(c+1) + ": " + str(count)
