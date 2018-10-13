f = open('A-large.in', 'r')
g = open('pancake_output.txt', 'w')

t = int(f.readline())

for case in xrange(t):
	input = f.readline().split()
	pancakes = list(map(lambda x: x == '+', input[0]))
	k = int(input[1])
	
	l = len(pancakes)
	flipcount = 0
	
	for flippos in xrange(l-k+1):
		if not pancakes[flippos]:
			for x in xrange(flippos, flippos+k):
				pancakes[x] = not pancakes[x]
			flipcount += 1
	
	outfirst = 'Case #' + str(case+1) + ': '
	outmid = str(flipcount) if all(pancake for pancake in pancakes) else 'IMPOSSIBLE'
	outlast = '\n' if case < t-1 else ''
	
	g.write(outfirst + outmid + outlast)
	