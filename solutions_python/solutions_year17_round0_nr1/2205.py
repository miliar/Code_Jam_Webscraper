in_f = open('A-large.in', 'r')
out_f = open('output1.txt', 'w')

def flip(pos, cakes, k):
	for i in range(k):
		if cakes[pos+i] == '+':
			cakes[pos+i] = '-'
		else:
			cakes[pos+i] = '+'
		#print cakes

line_count = 1
for line in in_f:
	count = 0
	toks = line.split(' ')
	if len(toks) == 1:
		continue
	k = int(toks[1])
	cakes = list(toks[0])
	#print k, cakes
	for i in xrange(len(cakes)-k+1):
		if cakes[i] == '+':
			continue
		else:
			flip(i, cakes, k)
			count += 1
	if cakes[i:] == ['+']*k:
		ans = 'Case #{}: {}\n'.format(line_count, count)
	else:
		ans = 'Case #{}: {}\n'.format(line_count, 'IMPOSSIBLE')

	out_f.write(ans)


	line_count += 1



