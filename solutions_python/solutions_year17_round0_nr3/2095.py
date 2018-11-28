#!/usr/bin/env python2
import sys

def find(seats):

	for x in xrange(len(seats)):
		if not seats[x][0]:
			break
	res = x

	for x in xrange(len(seats)):
		if seats[x][0]:
			continue
		Ls = seats[x][1]
		Rs = seats[x][2]
		if min(Ls, Rs) > min(seats[res][1], seats[res][2]):
			res = x
		elif min(Ls, Rs) == min(seats[res][1], seats[res][2]):
			if max(Ls, Rs) > max(seats[res][1], seats[res][2]):
				res = x
	return res

def recalculate(seats, p):
	L = len(seats)
	Lc = True
	Rc = True
	for x in xrange(1,L):
		l = p-x
		r = p+x
		Lc = Lc and (l >=0 ) and not seats[l][0]
		if Lc:
			seats[l] = (seats[l][0], seats[l][1], x-1)
		Rc = Rc and (r < L) and not seats[r][0]
		if Rc:
			seats[r] = (seats[r][0], x-1, seats[r][2])

	return seats

def solve(N, K):
	res = '%d %d' % (N, K)
	seats = []
	for x in xrange(N):
		seats.append((False, x, N-x-1))

	for x in xrange(K):
		p = find(seats)
		seats = recalculate(seats, p)
		seats[p] = (True,seats[p][1],seats[p][2])

	Ls = seats[p][1]
	Rs = seats[p][2]

	return (Ls,Rs)

cases = int(sys.stdin.readline())

for case in range(cases):
	line = [ int(x) for x in sys.stdin.readline()[:-1].split(' ')]
	N = line[0]
	K = line[1]
	r = solve(N, K)
	print ("Case #%d: %d %s" % (case+1,max(r[0],r[1]), min(r[0],r[1])))
