#!/usr/bin/env python
import math
import sys

def main():
	f = sys.stdin

	cases = int(f.readline().strip())
	for case in range(cases):
		k = int(f.readline().strip())
		s = f.readline().strip()
		
		best = len(s)
		perms = xpermutations(range(k))
		for perm in perms:
			score = 0
			last = 'X'
			for i in range(int(math.ceil(len(s) / float(k)))):
				block = s[i*k:(i+1)*k]
				for pos in perm:
					if pos >= len(block):
						continue
					c = block[pos]
					if c != last:
						score += 1
						last = c
			if score < best:
				best = score
			
		print "Case #%i: %i" % (case + 1, best)

def xcombinations(items, n):
	if n == 0:
		yield []
	else:
		for i in xrange(len(items)):
			for cc in xcombinations(items[:i] + items[i+1:], n-1):
				yield [items[i]] + cc
 
def xpermutations(items):
	return xcombinations(items, len(items))

if __name__ == "__main__":
	main()
