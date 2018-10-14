#!/usr/bin/python
import sys

def play_war(nao, ken):
	nao.sort(reverse=True)
	ken.sort()
	l, r = 0, len(ken)-1
	for b in nao:
		if b < ken[r]:
			r = r - 1
		else :
			l = l + 1
	return l

def play_dwar(nao, ken):
	nao.sort()
	ken.sort()
	l, r = 0, len(ken)-1
	for b in nao:
		if b < ken[l]:
			r = r - 1
		else :
			l = l + 1
	return l

t = int(sys.stdin.readline())
for case in xrange(1, t+1):
	sys.stdin.readline()
	nao = [float(x) for x in sys.stdin.readline().split()]
	ken = [float(x) for x in sys.stdin.readline().split()]

	war = play_war(nao, ken)
	dwar = play_dwar(nao, ken)

	print "Case #{}: {} {}".format(case, dwar, war)