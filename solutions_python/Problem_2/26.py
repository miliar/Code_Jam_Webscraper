# coding: euckr
import sys
sys.stdin = file(r'C:\Documents and Settings\ipkn\바탕 화면\B-large.in')
case_n = input()
for case in xrange(case_n):
	deltaT = input()
	sa, sb = (int(x) for x in raw_input().split())
	
	atob = []
	btoa = []

	for i in xrange(sa):
		f,t = raw_input().split()
		f,t = (int(x[0:2]) * 60 + int(x[3:5]) for x in (f,t))
		atob.append((f,t))

	for i in xrange(sb):
		f,t = raw_input().split()
		f,t = (int(x[0:2]) * 60 + int(x[3:5]) for x in (f,t))
		btoa.append((f,t))

	na = 0
	nb = 0
	atob.sort()
	btoa.sort()
	waita = []
	waitb = []
	while atob or btoa:
		if atob and (not btoa or atob[0][0] <= btoa[0][0]):
			l = [x for x in waita if x <= atob[0][0] ]
			if l:
				waita.remove(min(l))
			else:
				na += 1
			waitb.append(atob[0][1] + deltaT)
			atob.pop(0)
		else:
			l = [x for x in waitb if x <= btoa[0][0] ]
			if l:
				waitb.remove(min(l))
			else:
				nb += 1
			waita.append(btoa[0][1] + deltaT)
			btoa.pop(0)

	print "Case #%d: %d %d" % (case+1, na, nb)
