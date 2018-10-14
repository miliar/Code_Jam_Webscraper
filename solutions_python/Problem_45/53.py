''' Permuter from python cookbook: http://code.activestate.com/recipes/190465/'''

from __future__ import generators

def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc
            
def xselections(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for ss in xselections(items, n-1):
                yield [items[i]]+ss

def xpermutations(items):
    return xcombinations(items, len(items))


''' Now my code: '''

def score(P,perm):
	cells = [1] * P
	coins = 0
	for i in perm:
		cells[i] = 0
		j = i-1
		while j >= 0 and cells[j] == 1:
			coins +=1
			j -=1
		j = i+1
		while j < P and cells[j] == 1:
			coins +=1
			j +=1
	return coins
		


N = int(raw_input())

for Cs in xrange(1,N+1):
	P, Q = [int(i) for i in raw_input().split()]
	
	locs = [int(i) - 1 for i in raw_input().split()]
	
#	print P,Q,locs
	
	bs = P*P*P
	
	for i in xpermutations(locs):
		k =  score(P,i)		
		if k < bs: bs = k
	
	print "Case #%d: %d" % (Cs, bs)
	