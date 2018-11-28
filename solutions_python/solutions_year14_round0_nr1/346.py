import sys

TT = int(sys.stdin.readline())

for T in xrange(1,TT+1):
	a = int(sys.stdin.readline())
	r1 = set([ sys.stdin.readline() for i in range(4) ][a-1].split())
	a = int(sys.stdin.readline())
	r2 = set([ sys.stdin.readline() for i in range(4) ][a-1].split())
	
	join = r1.intersection(r2)

	if len(join) == 0: ans = "Volunteer cheated!"
	elif len(join) == 1: ans = list(join)[0]
	else: ans = "Bad magician!"

	print "Case #%d: %s" % (T, ans)

