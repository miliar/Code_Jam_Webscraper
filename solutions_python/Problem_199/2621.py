import sys

def swap(s,k):
	for i in range(k):
		s[i] = '-' if s[i]=='+' else '+'

def solve(s,k):
	x = 0
	while len(s)>0:
		if s[0]=='-':
			if len(s)<k:
				return None
			else:
				swap(s,k)
				x += 1
		s = s[1:]
	return x

lines = sys.stdin.readlines()

T = int(lines[0])
line = 1

for C in range(1,T+1):
	ss = lines[line].split()
	s = [c for c in ss[0] ]
	swaps = int(ss[1])
	line+=1

#	print(s, swaps)	
	sol = solve(s, swaps)
	print "Case #%d: %s" % (C, "IMPOSSIBLE" if sol is None else str(sol))
