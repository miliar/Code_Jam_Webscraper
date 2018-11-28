import os, sys
cases = open(sys.argv[1]).read().split('\n')[2::2]
cases = [ map(int,c.split(' ')) for c in cases]

cases_done = 0
for case in cases:
	cases_done += 1

	if len(case) <= 1:
		print 'Case #%d: NO'%(cases_done)
		continue
	
	case.sort(reverse=True)
	phillip_left  = [case[0]]
	phillip_right = [case[-1]]
	prefix = [case[0]]
	for e in case[1:]:
		prefix.append(prefix[-1] + e)
	for e in case[1:]:
		phillip_left.append( phillip_left[-1] ^ e)
	for e in case[-2::-1]:
		phillip_right.append( phillip_right[-1] ^ e)
	phillip_right = phillip_right[::-1]

	# Look for the optimum. greedy.
	best = -1
	for i in xrange(len(case)-1):
		if phillip_left[-2-i] == phillip_right[-1-i]:
			best = prefix[len(case) - i - 2]
			break

	if best == -1:
		print 'Case #%d: NO'%(cases_done)
	else:
		print 'Case #%d: %d'%(cases_done, best)
	
	'''	
	print 'real',case
	print 'pref',prefix
	print 'phle',phillip_left
	print 'phri',phillip_right
	print ''
	'''


