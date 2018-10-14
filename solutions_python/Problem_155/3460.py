from sys import argv

T = int(input())

for t in xrange(T):
	ppl = 0
	line = raw_input()
	smax = int(line.split(' ')[0])
	array = line.split(' ')[1]
	
	cum_sum = int(array[0])
	for s in xrange(smax):
		if cum_sum < (s+1) and int(array[s+1])>0:
			ppl += (s+1-cum_sum)
			cum_sum += ppl
		cum_sum += int(array[s+1])
	
	print 'Case #'+str(t+1)+': '+str(ppl)