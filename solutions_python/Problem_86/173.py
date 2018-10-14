import codecs
import sys
write = sys.stdout.write

def gcd(x, y):
	x = abs(x)
	y = abs(y)
	while y:
		x, y =  y, x % y
	return x
with codecs.open("C-small-attempt0.in", "r", "utf- 8") as f:
	temp = f.readlines()
	num = int(temp[0].strip())
	line = 1
	for i in xrange(num):
		t = temp[line].strip().split()
		N = int(t[0])
		L = int(t[1])
		H = int(t[2])
		line += 1
		d = []
		t2 = temp[line].strip().split()
		t2 = [int(q) for q in t2]
		t2.sort()
		f = False
		for w in xrange(L, H + 1):
			c = 0
			for n in t2:
				if n % w != 0 and w % n != 0:
					break
				else:
					c += 1
			if c == len(t2):
				print "Case #{0}: {1}".format(i + 1, w)
				f = True
				break
		if not f:
			print "Case #{0}: NO".format(i + 1)
#		for n in t2:
#			for m in t2:
#				ret = gcd(n, m)
#				if ret != 1 and ret not in d:
#					d.append(ret)
		line += 1
#print d
		
