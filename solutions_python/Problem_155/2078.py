import sys

sin = sys.stdin

T = int(sin.readline())
for i in range(T):
	line = sin.readline().split(' ')
	l = int(line[0])
	extra = 0
	total = int(line[1][0])
	for j in range(1, l+1):
		if total < j:
			this_round = (j - total)
			extra += this_round
			total += this_round + int(line[1][j ])
		else:
			total += int(line[1][j])
	print "Case #%d: %d" % (i + 1, extra)


    
