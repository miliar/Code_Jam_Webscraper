#!/usr/bin/env python
"""
StandingOvation.py

Josh Kaplan <jk@joshkaplan.org>

Problem Statement: https://code.google.com/codejam/contest/6224486/dashboard
"""
fname = 'A-large'
fin = open(fname + '.in', 'r')
fout = open(fname + '.out', 'w')
flog = open(fname + '.log', 'w')

# the number of cases
N = int(fin.readline())

for i in range(0, N):
	data = fin.readline().split(' ')
	S_max = int(data[0])
	S = data[1].replace('\n', '')
	print >> flog, S_max, S

	ppl_standing = 0
	friends = 0

	for j in range(0, S_max + 1):
		print >> flog, '>> ppl_standing:', ppl_standing
		while ppl_standing < j:
	 		friends = friends + 1
	 		ppl_standing = ppl_standing + 1
	 	ppl_standing = ppl_standing + int(S[j])
	 	print >> flog, 'DEBUG >>>', j, ppl_standing, friends
	
	print "Case #{x}: {y}".format(x=i+1, y=friends)
	print >> fout, "Case #{x}: {y}".format(x=i+1, y=friends)
