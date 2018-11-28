# Solution to "Fair and Square" for Google Code Jam 2013
# by Peter Mattsson (quantum.caffeine@gmail.com)
import sys
import string
from math import sqrt

with open(sys.argv[1], 'r') as f:
	numCases = int(f.readline())
	cases = [tuple(int(x) for x in line.split()) for line in f]

f = open(sys.argv[2], 'w')

def is_pal(n):
	pal_str = str(n)
	chunk = len(pal_str)/2
	return pal_str[:chunk] == pal_str[-1:-(chunk+1):-1]

for n,(a,b) in enumerate(cases):
	p, total = 0, 0
	start_digits = len(str(int(sqrt(a))))/2
	if start_digits == 0:
		p = 1
	else:
		p = 10**(start_digits-1)
	end_digits = len(str(int(sqrt(b))))/2
	if end_digits == 0:
		end_p = 10
	else:
		end_p = 10**(end_digits)
	while p < end_p:
		base_pal = str(p)
		for pal in (int(base_pal + base_pal[-2::-1]), int(base_pal + base_pal[::-1])):
			test_pal = pal**2
			if is_pal(test_pal):
				if a <= test_pal <= b:
					total += 1
		p += 1
	f.write("Case #%d: %d\n"%(n+1, total))

f.close()