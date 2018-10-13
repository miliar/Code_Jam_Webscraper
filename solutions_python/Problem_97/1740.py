from itertools import *

cases = int(raw_input())

def recycled_pairs(n):
	l = [int(d) for d in str(n)]

	for i in range(len(l) - 1):
		l = [l[-1]] + l[:-1]
		m = int("".join([str(d) for d in l]))
		
		if l[0] != 0:
			yield (n, m)
		
for i in range(1, cases + 1):
	(a, b) = [int(n) for n in raw_input().split(" ")]
	
	valid_pairs = {}
	
	for k in range(a, b + 1):
		for n, m in recycled_pairs(k):				
			if a <= n < m <= b:
				valid_pairs[(n, m)] = True
				
	print "Case #%d: %d" % (i, len(valid_pairs))