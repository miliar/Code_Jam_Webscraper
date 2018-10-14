import sys
from collections import deque
line_number = 0

def algo(line):
	s, k = line.split()
	s = list(s); k = int(k)
	# walk along pancake line, flipping as needed
	flipsUB = len(s) - k + 1
	offset = 0
	flipsActual = 0
	while offset < flipsUB:
		if s[offset] == "-":
			for cake in range(offset, offset+k):
				s[cake] = "+" if s[cake] == "-" else "-"
			flipsActual += 1
		offset += 1
	# check last k-1 cakes for negativity
	for cake in s[flipsUB:]:
		if cake == "-":
			return "IMPOSSIBLE"
	return str(flipsActual)

for line in sys.stdin:
	if line_number:
		x = algo(line)
		print("Case #%d: %s" % (line_number, x))
	line_number += 1


"""
3
-+-+-
+-++-
++---
+++++

IMPOSSIBLE:
--+- 2
-+-- 3
---- 3

"""
