def next(num):
	blah = [int(i) for i in perms(str(num))]
	while 1:
		blah.sort()
		for a in blah:
			if a > num:
				return a
		blah = [int(i) for i in perms(str(num)+"0")]
	return num

def listify(str):
	a = [0 for i in xrange(9)]
	for i in str:
		if i == "0":
			continue
		a[int(i)-1] += 1
	return a

def perms(blah):
	if len(blah) == 1:
		return [blah]
	res = []
	for p in perms(blah[1:]):
		for i in xrange(len(p)+1):
			res.append(p[:i] + blah[0] + p[i:])
	return res

T = int(raw_input())
for i in xrange(T):
	num = int(raw_input())
	print "Case #%d: %d" % (i+1, next(num))
