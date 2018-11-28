import sys

sys.stdin = open("B-small-attempt0 (1).in")

lines = [line.strip() for line in sys.stdin]
total = int(lines.pop(0))
i = 0

while i < total:
	a, b, k = map(int, lines[i].split())
	nums = 0
	numSet = set()
	for j in xrange(0, a):
		for l in xrange(0, b):
			ans = j & l
			if ans < k:
				nums+=1
	print "Case #" + str(i + 1) + ": " + str(nums)
	i += 1
