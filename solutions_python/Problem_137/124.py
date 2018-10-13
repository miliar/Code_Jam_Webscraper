#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
# google code jam - c.durr- 2014

# MinesweeperMaster
# https://code.google.com/codejam/contest/2974486/dashboard#s=p2
 
def readint():    return int(raw_input())
def readarray(f): return map(f, raw_input().split())

def transpose(M):
	if M==None or M==[]:
		return M
	rows = len(M)
	cols = len(M[0])
	return [[M[i][j] for i in range(rows)] for j in range(cols)]

# fill row by row at most nb bombs
def fill(T, startrow, countrow, startcol, countcol, nb):
	# I know, count row is not used, just here fore symmetry
	for k in range(nb):
		i = startrow + k/countcol
		j = startcol + k%countcol
		T[i][j] = '*'

# special case of the 3 by 3 grid
G = [ ['...',
       '...',
       '..c'],
       ['*..',
        '...',
        '..c'],
       None,
       ['***',
        '...',
        '..c'],
       None,
       ['***',
        '*..',
        '*..c'],
        None,
        None,
       ['***',
        '***',
        '**c']  ]


def solve(r,c,m):
	if r>c:
		return transpose(solve(c,r,m))
	T = [['.']*c for i in range(r)]
	T[r-1][c-1] = 'c'
	if m==r*c-1:
		fill(T,0,r,0,c,m)
		return T
	if r==1:
		fill(T, 0, 1, 0, c, m)
		return T
	if r==2:
		if m%2==1 or m>c*2-4:
			return None
		fill(T, 0, 2, 0, m/2, m)
		return T
	if m<=(r-2)*(c-2):
		fill(T, 0, r-2, 0, c-2, m)
		return T
	if m<r*c-9:
		a = (r-2)*(c-2) - (m - (r-2)*(c-2))%2
		fill(T, 0, r-2, 0, c-2, a)
		b = min(m-a, 2*(r-3))
		fill(T, 0,   r-3, c-2, 2,   b)
		fill(T, r-2, 2,   0,   (m-a-b)/2,	 m-a-b  )
		return T
	fill(T,0,r,0,c,r*c)
	s = G[m-r*c]
	if s==None:
		return None
	for i in range(3):
		for j in range(3):
			T[r-3+i][c-3+j] = s[i][j]
	return T

for test in range(readint()):
	r,c,m = readarray(int)
	t = solve(r,c,m)
	print "Case #%i:"% (test+1)
	if t==None:
		print "Impossible"
	else:
		t[r-1][c-1] = 'c'
		for row in t:
			print ''.join(row)
