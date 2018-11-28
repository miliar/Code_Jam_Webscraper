import sys, math

def solve(line, case):
	n, d, g = tuple([int(i) for i in line])
	if (g==100 and d!=100) or (g==0 and d!=0):
		print "Case #%s: Broken" % case
		return
	nl = int(math.ceil(100.0/d)) if d!=0 else 1
	for D in xrange(nl,n+1):
		if (d*D)%100!=0:
			continue
		print "Case #%s: Possible" % case
		break
	else:
		print "Case #%s: Broken" % case
		

with open(sys.argv[1]) as fp:
	cases = int(fp.readline())
	for i in range(1,cases+1):
		solve(fp.readline().strip().split(),i)
