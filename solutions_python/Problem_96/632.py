import sys

for i in range(0, int(sys.stdin.readline().strip())):
	line = (int(x) for x in sys.stdin.readline().strip().split(' '))
	googlers, surprising, p, scores = next(line), next(line), next(line), tuple(line)
	total = 0
	for score in scores:
		if 3 * p - 2 <= score:
			total += 1
		elif surprising and 3 * p - 4 > 0 and 3 * p - 4 <= score:
			surprising = surprising - 1
			total += 1
	print("Case #%d: %d" % (i + 1, total))
