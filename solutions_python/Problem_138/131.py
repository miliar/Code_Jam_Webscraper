#! /usr/bin/python

import sys
import math

def ken_choose(wn, Wk):
	if wn > max(Wk):
		return min(Wk)
	else:
		for wk in Wk:
			if wk>wn:
				return wk
	assert 0, "Shouldnt go here"

def play(wn, Wn, wk, Wk):
	Wn.remove(wn)
	Wk.remove(wk)
	if wn>wk:
		return 1
	else:
		return 0

def exec_test(Wn, Wk):
	sc1=0
	sc2=0
#	print "Wn = %s" % Wn
#	print "Wk = %s" % Wk

	Wn_save = list( Wn )
	Wk_save = list( Wk )

	while len(Wn)>0:
		wn = max(Wn)
		wk = ken_choose(wn, Wk)
		sc2 += play(wn, Wn, wk, Wk)

	Wn = list( Wn_save )
	Wk = list( Wk_save )

	while len(Wn)>0:
		if max(Wn) < min(Wk):
			wn = min(Wn)
			wn_sd = wn
		else:
			for _wn in Wn:
				if _wn>min(Wk):
					wn = _wn
					wn_sd = (1.0+max(Wk))/2
					break
		wk = ken_choose(wn_sd, Wk)
		sc1 += play(wn, Wn, wk, Wk)


	return " %i %i" % (sc1, sc2)

# ====== READ INPUT ====================================

assert len(sys.argv)>=2, "Need input file"
input_file = sys.argv[1]
fd = open(input_file, 'r')
fd_out = open(input_file+".out", 'w')
n = int(fd.readline().split()[0]) # Number of tests
for test in xrange(n):
	print "=== Test #%i ===" % (test+1)
	N = int(fd.readline().split()[0])
	nums = fd.readline().split()
	Wn = sorted( map(lambda x: float(x), nums) )
	nums = fd.readline().split()
	Wk = sorted( map(lambda x: float(x), nums) )
	ret = exec_test(Wn, Wk)
	strret = "Case #%i:%s" % ((test+1), str(ret))
	print strret
	fd_out.write(strret+"\n")

