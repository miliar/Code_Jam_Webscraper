import sys
import pickle

def recycles(n):
	ds = str(n)
	w = len(ds)
	r = set()
	for i in range(1,w):
		s = ds[i:]+ds[:i]
		if len(str(int(s))) == w and int(s) > n:
			r.add(int(s))
	return r

rls = [0]
for i in range(2000000):
	rls.append(recycles(i+1))	

T = int(sys.stdin.readline().strip())

for i in range(T):
	A, B = [int(w) for w in sys.stdin.readline().split()]
	c = 0
	for n in range(A, B+1):
		for m in rls[n]:
			if m <= B:
				c+=1
	
	print "Case #%d: %d"%(i+1, c)
