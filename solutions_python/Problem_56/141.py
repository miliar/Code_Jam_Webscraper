#!/usr/bin/env python

# Google code jam 2010 : rotate

import sys

def result(r,k,rows):
    rot = [['*' for i in range(r)] for i in range(r)]
    for i in range(r):
	for j in range(r):
	    rot[j][i] = rows[r-1-j][i]

    for j in range(r):
	p = rot[j].count('.')
	for z in range(p):
	    rot[j].remove('.')
	rot[j] = ['.' for i in range(p)] + rot[j]

    table = [['*' for i in range(r)] for i in range(r)]
    for i in range(r):
	for j in range(r):
	    table[i][j] = rot[j][i]

    p,q = nicek(table,k,r)
    if p and not q:
	return "Red"
    elif p and q:
	return "Both"
    elif q and not p:
	return "Blue"
    else:
	return "Neither"

def nicek(t,k,r):
    red = False
    blue = False
    for i in range(r):
	for j in range(r):
	    if not red:
		red = find(t,i,j,r,k,'R')
	    if not blue:
		blue = find(t,i,j,r,k,'B')
    return (red,blue)
	    
def find(t,i,j,r,k,char):
    try:
	if t[i][j] == char:
	    # horiz
	    k1 = 1
	    for f in range((j+1),r):
		if t[i][f] == char:
		    k1 = k1 + 1
		    if k1 >= k:
			raise NameError('')
		else:
		    break
	    # verti
	    k1 = 1
	    for f in range((i+1),r):
		if t[f][j] == char:
		    k1 = k1 + 1
		    if k1 >= k:
			raise NameError('')
		else:
		    break
	    # diago1
	    k1 = 1
	    for f in range(min(r-1-i,r-1-j)):
		if t[i+f+1][j+f+1] == char:
		    k1 = k1 + 1
		    if k1 >= k:
			raise NameError('')
		else:
		    break
	    # diago2
	    k1 = 1
	    for f in range(min(i,r-1-j)):
		if t[i-f-1][j+f+1] == char:
		    k1 = k1 + 1
		    if k1 >= k:
			raise NameError('')
		else:
		    break

	    return False
	else:
	    return False
    except NameError:
	return True


p = int(sys.stdin.readline())
cases = []
for s in range(1,p+1):
    line = sys.stdin.readline()
    r,_,k = line.partition(' ')
    r = int(r)
    k = int(k)

    rows = [[] for i in range(r)]
    for i in range(r):
	line = sys.stdin.readline()
	for j in range(r):
	    rows[i].append(line[j])

    print "Case #" + str(s) + ": " +  str(result(r,k,rows))

