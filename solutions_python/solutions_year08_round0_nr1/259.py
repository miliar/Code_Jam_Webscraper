# Google CodeJam 2008
# Qualification round - problem 1
# autor: HighEgg
import sys

input = open(sys.argv[1],'r')
ncases = int(input.readline())
for icase in range(ncases):
    icase += 1
    nengs = int(input.readline())
    emap = {}
    for i in range(nengs):
	eng = input.readline().rstrip()
	emap[eng] = i
    nqrs = int(input.readline())
    qrs = [emap[input.readline().rstrip()] for i in range(nqrs)]
    sw = [0]*nengs
    for q in reversed(qrs):
	sm = min(sw)
	sw1 = [min(s,sm+1) for s in sw]
	sw1[q] = min(sw[e] for e in range(nengs) if e != q) + 1
	sw = sw1
	    
    print 'Case #'+str(icase)+':',min(sw)

