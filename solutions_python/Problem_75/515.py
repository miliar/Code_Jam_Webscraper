import sys

T = int(sys.stdin.readline())

def gg(data):
	N = int(data[0])
	R = data[1:1+N]
	data[:] = data[1+N:]
	return R
	
def two(x):
	return "".join(sorted([x[0],x[1]]))

for case in range(T):
	print "Case #%d: " % (case+1),
	
	data = sys.stdin.readline().strip().split(' ')
#	print data
	comb = [(two(x), x[2]) for x in gg(data)]
	comb = dict(comb)
	conf = set([two(x) for x in gg(data)])
	inv = gg(data)
#	print comb, conf, inv
	t = ""
	for x in inv[0]:
		t += x
#		print t
		while len(t) >= 2:
			cc = two(t[-2:])
			if comb.has_key(cc):
				t = t[:-2] + comb[cc]
#				print "comb: " + t
			else:
				break
		for c in conf:
			if c[0] in t and c[1] in t:
				t = ""
#				print "conf: " + c
				break
	print "[" + ", ".join(list(t)) + "]"
	
	