from fractions import gcd

def cf(freq, f):
	if f == 1:
		return True
	for _f in freq:
		if f > _f:
			if f%_f != 0:
				return False
		else:
			if _f%f != 0:
				return False
	return True

# harmony
def harm(freq, l, h):
	for f in range(l, h+1):
		if cf(freq, f):
			return f
	return None
	
f = open("C.in")
t = int(f.readline())
for _t in range(t):
	n,l,h = map(int, f.readline().split())
	freq = map(int, f.readline()[:-1].split())
	c = harm(freq, l, h)
	if not c:
		print "Case #{0}: NO".format(_t+1)
	else:
		print "Case #{0}: {1}".format(_t+1, c)
f.close()
