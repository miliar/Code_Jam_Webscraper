#!/usr/bin/python
'''
Google codejam template
https://code.google.com/codejam/contest/1460488/dashboard#s=p1
'''
import sys
#fh = sys.stdin
fh = open(sys.argv[1])

cases = int(fh.readline())

totals = [ # (max p (no surprise), max p with surprise)
	(0,0), # 0
	(1,1),
	(1,1),
	]
for i in range(1, 9):
	totals.append((i,i+1))
	totals.append((i+1,i+1))
	totals.append((i+1,i+2))
totals += [
	(9,10), # 9*3 = 27
	(10,10),
	(10,10),
	(10,10), # 10*3 = 30
	]

for case in range(1, cases+1):
	print 'Case #%i:' % case,
	line = [ int(i) for i in fh.readline().split() ]
	n = line[0] # number of contestants
	s = line[1] # count surprising
	p = line[2] # points total to find (>=)
	t = line[3:] # total for each contentant
	gg = 0 # good googlers with score >= p
	for i in t:
		if totals[i][0] >= p:
			gg += 1
		elif s and totals[i][1] >= p:
			gg += 1
			s -= 1
		else:
			pass
	print gg
