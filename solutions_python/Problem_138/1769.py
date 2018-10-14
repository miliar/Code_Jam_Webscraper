#!/usr/bin/python

import sys

T = int(sys.stdin.readline().strip())

def play_war(naomi,ken,N):
	ken_score = 0
	for i in xrange(N):
		chosen_naomi = naomi[i]
		for j in xrange(N):
			if chosen_naomi < ken[j] and ken[j] != 1:	
				ken_score = ken_score + 1
				naomi[i] = 1
				ken[j] = 1
				break	
	return (N-ken_score)

def basic_naomi_score(naomi,ken,N):
	for x in xrange(N):
		for y in xrange(N):
			if naomi[x] > ken[y] and naomi[x] != 1:
				naomi[x] = 1
				ken[y]  = 1
	if sum(naomi) == N: return 0
	else: return 1

def play_dwar(naomi,ken,N):
	ken_score = 0
	flag = 1
	stop_check = 0
        for i in xrange(N):
		if flag:
			flag = basic_naomi_score(naomi[:],ken[:],N)
        		if flag == 0: break
			chosen_naomi = naomi[i]
                	for j in xrange(N-1,-1,-1):
				if j != 0 and chosen_naomi < ken[j-1]:
					told_naomi = ken[j-1] + 0.00045
				else:
					told_naomi = chosen_naomi
				if told_naomi < ken[j] and ken[j] != 1:
					ken_score = ken_score + 1
					naomi[i] = 1
					ken[j] = 1
					break
        return (N-ken_score)

for i in xrange(T):
	dwar_score = 0
	war_score = 0
	naomi = []
	ken = []
	N = int(sys.stdin.readline().strip())
	naomi = map(float,sys.stdin.readline().strip().split()) 
	ken = map(float,sys.stdin.readline().strip().split())
	naomi.sort()
	ken.sort()
	dwar_score = play_dwar(naomi[:],ken[:],N)
	war_score = play_war(naomi[:],ken[:],N)

	print "Case #%d: %d %d" %(i+1, dwar_score, war_score)
