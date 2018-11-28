# Google CodeJam 2017 - Qualification Round
# Problem B. Tidy Numbers
# Author: Mahmoud Aladdin <aladdin3>

import sys

def solve(cn):
	n = [ord(x) - ord('0') for x in raw_input().strip()]
	
	for i in xrange(len(n) - 2, -1, -1):
		if n[i] > n[i + 1]:
			n[i] -= 1
			for j in xrange(i + 1, len(n)):
				n[j] = 9
	
	res = 0
	for i in xrange(len(n)):
		res *= 10
		res += n[i]
	
	print "Case #%d: %d" % (cn, res)
	
	return

if __name__ == "__main__":
	tc = input()
	for i in xrange(tc):
		solve(i + 1)
