import sys

def avg(n, p):
	assert n>=0
	if p == 0:
		return True, False
	if p == 1:
		if n >= 1:
			return True, False
		else:
			return False, False
	if n >= 3*p-2:
		return True, False
	if n < 3*p-4:
		return False, False
	return True, True

T = int(sys.stdin.readline().strip())

for i in range(T):
	line = [int(w) for w in sys.stdin.readline().split()]
	N,S,p = line[:3]
	scores = line[3:]

	c = 0
	for s in scores:
		ok, sp = avg(s, p)
		if sp:
			if S == 0:
				continue
			else:
				S-=1
				c+=1
		else:
			if ok:
				c+=1

	
	print "Case #%d: %d"%(i+1, c)

