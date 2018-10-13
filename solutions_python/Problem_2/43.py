#!/usr/bin/python

def decode(s):
	h, m = s.split(":")
	return int(h) * 60 + int(m)

n = int(raw_input())
for i in xrange(1,n+1):
	t = int(raw_input())
	na, nb = raw_input().split()
	na, nb = int(na), int(nb)
	ad, aa, bd, ba = [], [], [], []
	for j in xrange(na):
		td, ta = raw_input().split()
		ad.append(decode(td))
		aa.append(decode(ta))
	for j in xrange(nb):
		td, ta = raw_input().split()
		bd.append(decode(td))
		ba.append(decode(ta))
	ad.sort()
	aa.sort()
	bd.sort()
	ba.sort()
	ad.reverse()
	bd.reverse()

	resulta = na
	for arrive in ba:
		while len(ad):
			if ad.pop() >= arrive + t:
				resulta = resulta - 1
				break

	resultb = nb
	for arrive in aa:
		while len(bd):
			if bd.pop() >= arrive + t:
				resultb = resultb - 1
				break
	print "Case #%d: %d %d" % (i, resulta, resultb)
