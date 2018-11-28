#!/usr/bin/python

nb = int(raw_input())

def get_max(tab):
	j = 0
	for i in xrange(len(tab)):
		if tab[i] > tab[j]:
			j = i

	return j

for num in xrange(1, nb+1):
	N, K = [ int(i) for i in raw_input().split() ]
#	print N, K
	stalls = [1] + [0] * N + [1]
	inter = [N]
#	print inter
	for i in xrange(K):
		m = get_max(inter)
		inter[m] -= 1
		p1 = inter[m]//2
		p2 = inter[m] - p1
		inter = inter[:m] + [p1] + [p2]+ inter[m+1:]
#		print inter

	print "Case #{}: {} {}".format(num, max(p1, p2), min(p1, p2))
#	if num == 3:
#		break
