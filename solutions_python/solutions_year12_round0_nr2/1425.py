import sys
	
inp = sys.stdin.readlines()
T = int(inp[0])

for i in range(1, T + 1):
	case = [int(t) for t in inp[i].split(' ')]
	n = case[0]
	S = case[1]
	p = case[2]
	
	C1 = 0
	C2 = 0
	for j in range(0, n):
		score = case[3 + j]
		a = int(score / 3)
		r = score % 3
		if (r != 0):
			a = a + 1
		if a >= p:
			C1 = C1 + 1
		else:
			if r == 2 or (r == 0 and a > 0):
				a = a + 1
			if a >= p:
				C2 = C2 + 1
				
	print 'Case #%d: %s' % (i, C1 + min(S, C2))
	