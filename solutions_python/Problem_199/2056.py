"""
3
---+-++- 3
+++++ 4
-+-+- 4
"""


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n, k = [s for s in raw_input().split(" ")]
	c = 0
	k = int(k)
	for j in range(len(n)-(k-1)):
		if n[j] == '-':
			s = ""
			for p in n[j:j+k]:
				s += '-' if p =="+" else "+"
			n = n[:j] + s + n[j+k:]
			c += 1	
	if "-" in n:
		c = "IMPOSSIBLE"

	print "Case #{}: {}".format(i, c)