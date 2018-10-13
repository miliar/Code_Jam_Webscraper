import sys

T = int(sys.stdin.readline())

for case in range(1,T+1):
	N,L,H = [ int(x) for x in sys.stdin.readline().split() ]
	O = [ int(x) for x in sys.stdin.readline().split() ]
	
	res = -1
	possible = False
	
	for f in range(L,H+1):
		res = f
		p = True
		for o in O:
			if not (f % o == 0 or o % f == 0):
				p = False
				break
		if p:
			possible = True
			break
	
	print "Case #%d: %s" % (case, possible and res or "NO")