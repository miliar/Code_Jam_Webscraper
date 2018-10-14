#! /usr/bin/python

import sys


def spin(N,K,inp):
	out = [['.' for j in xrange(N)] for i in xrange(N)]
	for i in xrange(N):
		for j in xrange(N):
			out[j][N-i-1] = inp[i][j]
	return out
def drop(N,K,inp):
	out = [list() for i in xrange(N)]
	for i in xrange(N):
		for j in xrange(N):
			x = inp[i][j]
			if x == '.':
				out[j].insert(0,x)
			else:
				out[j].append(x)
	return out
def checka(N,K,spun,who,a,b):
	for i in xrange(K):
		if b+i >= N: return False
		if spun[a][b+i] != who: return False
	return True
def checkb(N,K,spun,who,a,b):
	for i in xrange(K):
		if a+i >= N: return False
		if b+i >= N: return False
		if spun[a+i][b+i] != who: return False
	return True
def check(N,K,spun,who,a,b):
	return checka(N,K,spun,who,a,b) or checkb(N,K,spun,who,a,b)
def who(N,K,spun):
	red,blue = False, False
	for i in xrange(N):
		for j in xrange(N):
			if check(N,K,spun,'R',i,j): red= True
			if check(N,K,spun,'B',i,j): blue= True
			if red and blue: return "Both"
	spun = spin(N,K,spun)
	for i in xrange(N):
		for j in xrange(N):
			if check(N,K,spun,'R',i,j): red= True
			if check(N,K,spun,'B',i,j): blue= True
			if red and blue: return "Both"
	if red and blue: return "Both"
	if red: return "Red"
	if blue: return "Blue"
	return "Neither"


if __name__ == "__main__":
	cases = int(sys.stdin.readline())
	for case in xrange(1,cases+1):
		N,K = map(int, sys.stdin.readline().strip().split())
		initial = []
		for i in xrange(N):
			initial.append(sys.stdin.readline().strip())
		spun = spin(N,K,initial)
		dropped = drop(N,K,spun)
		ftw = who(N,K,dropped)
		print "Case #%d: %s" % (case, ftw)
