def generateperm(k, n):
	opts = range(1, k+1)
	perm = []
	z = n
	y = k
	while(len(opts) > 0):
		perm += [opts[z % y]]
		opts.remove(opts[z % y])
		z /= y
		y -= 1
	return perm
	
def actcompress(perm, s):
	s1 = s
	res = ""
	while s1 != "":
		for i in perm:
			res += s1[i-1]
		s1 = s1[len(perm):]
	
	count = 1
	for i in range(1, len(res)):
		if(res[i] != res[i-1]): count += 1
	return count

def fact(n):
	if(n == 1): return 1
	return n*fact(n-1)

def compress(k, s):
	minc = 100000
	for z in range(fact(k)):
		perm = generateperm(k, z)
		c = actcompress(perm, s)
		if(c < minc): minc = c
	return minc

n = int(raw_input())
for i in range(n):
	k = int(raw_input())
	s = raw_input()
	print "Case #%d: %d" % (i+1, compress(k, s))
	
