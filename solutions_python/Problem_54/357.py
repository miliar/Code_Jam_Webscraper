import sys

lines = sys.stdin.readlines()

def gcf(l):
	l.sort()
	while (l[0]==0):
		l = l[1:]
	ll = []
	for i in l[1:]:
		j = i % l[0]
		if j: ll.append(j)
	ll.append(l[0])
	return ll
	
C = int(lines[0])
for c in range(C):
	t = [int(x) for x in lines[c+1].split()[1:]]
	t.sort()
	dt = [x-t[0] for x in t[1:]]
	while (len(dt) > 1):
		dt = gcf(dt)
	m = dt[0]
	k = int(t[0]/m)
	p = -t[0] + k*m
	while(p <0):
		p += m

	print "Case #%d: %ld" % (c+1, p)
	
