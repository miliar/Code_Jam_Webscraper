import sys

def solve(s):
	standing = 0
	need = 0

	for (i, Si) in enumerate(s):
		if Si > 0:
			if standing >= i: # Are there enough people standing already?
				standing += Si
			else: # We need to invite more.
				need += i - standing
				standing += Si + (i - standing)
	
	return need


f = open(sys.argv[1])
t = int(f.readline())

for _t in range(t):
	s = f.readline().split()[1]
	s = [int(s[i]) for i in range(len(s))]
	#n = doit(points)
	print("Case #%d: %d" % (_t+1, solve(s)))