#!/usr/bin/python
# Google Code Jam 2011, Round 1B: RPI
from __future__ import division
import sys

T = int(sys.stdin.readline())
for case in xrange(1, T+1):
	print 'Case #{0}:'.format(case)	
	N = int(sys.stdin.readline())
	opps = [[] for team in range(N)]
	wp = []
	owp = []
	rpi = []
	for team in xrange(N):
		winlist = []
		gamelist = []
		wps = {}
		for opp, game in enumerate(sys.stdin.readline().strip()):
			if game == '1':
				winlist.append(1)
				gamelist.append(1)
				opps[team].append(opp)
			elif game == '0':
				winlist.append(0)
				gamelist.append(1)
				opps[team].append(opp)
			elif game == '.':
				winlist.append(0)
				gamelist.append(0)
		wps[team] = sum(winlist)/sum(gamelist)
		for opp in xrange(N):
			if gamelist[opp] == 1:
				wps[opp] = sum([winlist[x] for x in range(len(winlist)) if x!=opp])/(sum(gamelist)-1)
		wp.append(wps)
	for team in xrange(N):
		owp.append(sum(wp[o][team] for o in opps[team])/len(opps[team]))
	for team in xrange(N):
		oowp = sum(owp[o] for o in opps[team])/len(opps[team])
		print 0.25*wp[team][team] + 0.5*owp[team] + 0.25*oowp
