import sys

with open('A-large.in') as f:


	T = int(f.readline())
	for t in xrange(T):
		line = f.readline().split()
		s_max = int(line[0])
		dudes = line[1]
		ans = 0
		total_seen = 0
		for i in xrange(s_max + 1):
			total_seen += int(line[1][i])
			if total_seen < i + 1:
				ans += i + 1 - total_seen
				total_seen += i + 1 - total_seen
		print "Case #" + str(t + 1) + ": " + str(ans)
