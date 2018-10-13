#!/usr/bin/python

def readfloats(f):
	return sorted(map(float, f.readline().strip().split()))
	
	
def war(naomi, ken):
	n = len(naomi)
	score = 0
	j = 0
	k = n - 1
	for i in xrange(n - 1, -1, -1):
		if naomi[i] > ken[k]:
			score += 1
			j += 1
		else:
			k -= 1
	return score

def deceitfulWar(naomi, ken):
	n = len(naomi)
	j = 0
	k = n - 1
	score = 0
	for i in xrange(n):
		if naomi[i] > ken[j]:
			score += 1
			j += 1
		else:
			k -= 1
	return score

f = open("d.in", "rt")

T = int(f.readline().strip())
for tc in xrange(1, T + 1):
	n = int(f.readline().strip())
	naomi = readfloats(f)
	ken = readfloats(f)
	print "Case #%d: %d %d" % (tc, deceitfulWar(naomi, ken), war(naomi, ken))

f.close()
