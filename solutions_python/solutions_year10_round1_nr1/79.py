#!/usr/bin/env python

dir = ( (1,0), (0,1), (1,-1), (1,1) )

t = int(raw_input())
for case in xrange(1,t+1):
	n,k = tuple([int(x) for x in raw_input().split()])
	a = []
	for i in xrange(n):
		a.append(raw_input())
		s = ''.join(a[i].split('.'))
		s = '.' * (n - len(s)) + s
		a[i] = s
#		print a[i]

	win = [0, 0]	# red, blue
	for i in xrange(n):
		for j in xrange(n):
			colour = a[i][j]
			if colour not in ('R', 'B'):
				continue
#			print colour

			cou = [0 for c in xrange(4)]
			coo = [ [i,j] for c in xrange(4)]
#			print coo
			for s in xrange(k-1):
				for d in xrange(4): #directions
					coo[d][0] += dir[d][0]
					coo[d][1] += dir[d][1]
					if coo[d][0] >= 0 and coo[d][0] < n and coo[d][1] >= 0 and coo[d][1] < n:
						if a[coo[d][0]][coo[d][1]] == colour:
							cou[d] += 1
#			print cou
			for c in cou:
				if c == (k - 1):
					if colour == 'R':
						win[0] = 1
					else:
						win[1] = 1

	ans = 'Neither'
	if win[0] == 1 and win[1] == 1:
		ans = 'Both'
	elif win[0] == 1:
		ans = 'Red'
	elif win[1] == 1:
		ans = 'Blue'

	print "Case #%d: %s" % (case, ans)
