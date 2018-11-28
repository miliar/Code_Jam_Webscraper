import math
cache = {0: [], 1:[0,1,2], 2:[11, 22]}
def genNums(digits):
	global cache
	if digits <= 2:
		return cache[digits]
	if (digits) in cache:
		return cache[digits]
	mids = genNums(digits-2)
	midz = ("0")*(digits-2)
	m = 10**(digits-1)
	ret = [m+1, 2*m + 2]
	for i in mids:
		toadd = m + 10*i + 1
		ret.append(toadd)
		toadd = 2*m + 10*i + 2
		ret.append(toadd)
	actualret = []
	for r in ret:
		s = str(r*r)
		if s == s[::-1]:
			actualret.append(r)
	cache[digits] = actualret
	return actualret
	
vals = [0, 1, 4, 9]
for i in xrange(2, 51):
	ns = genNums(i)
	for n in ns:
		vals.append(n*n)

f = open("fair.in")

c = int(f.readline().strip())
for i in xrange(c):
	lread = f.readline().strip().split(" ")
	left = int(lread[0])
	right = int(lread[1])
	ctr = 0
	for v in vals:
		if v >= left:
			if v <= right:
				ctr = ctr + 1
			else:
				break
	print "Case #"+str(i+1)+": "+str(ctr)

f.close()
