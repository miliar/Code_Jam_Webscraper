import math

f = open("c.in")
data = f.read()
f.close()

data = data.split("\n")

t = int(data[0])

def bin(n, size):
	l = []
	while n > 0:
		l += [(n%2 == 1)]
		n /= 2
	l += [False] * (size - len(l))
	return l

def sum2(l):
	N = int(math.log(max(l), 2)) + 1
	if len(l) == 0: return 0
	v = bin(l[0], N)
	for e in l[1:]:
		toAdd = bin(e, N)
		for i in xrange(len(v)):
			v[i] = v[i] ^ toAdd[i]
	s = 0
	for i in xrange(len(v)):
		s += v[i] * 2**i
	return s

def solve(l):
	maxv = -1
	n = len(l)
	for i in xrange(1, 2**n-1):
		sep = bin(i, n)
		l1 = [l[j] for j in xrange(n) if sep[j]]
		l2 = [l[j] for j in xrange(n) if not sep[j]]
		if sum2(l1) == sum2(l2):
			maxv = max(maxv, sum(l1))
	if maxv == -1: return "NO"
	return str(maxv)

f = open("c.out", "w")
for ti in xrange(t):
	l = data[2+ti*2].split(" ")
	l = [int(e) for e in l]
	
	#print l
	
	S = "Case #%d: %s" % ((ti+1), solve(l))
	print S
	f.write("%s\n" % S)
f.close()

