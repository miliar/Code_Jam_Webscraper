from itertools import *

infile = "A-large.in"

lines = [s.rstrip() for s in open(infile, "rb").readlines()]
NCases=int(lines[0])

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

for i,caseline in enumerate(lines[1:]):
	l = caseline.split(" ")
	nbuttons = int(l[0])
	#print nbuttons
	bothlist = [(c,int(n)) for c, n in grouper(2, l[1:])]
	olist = [n for c, n in bothlist if c == 'O']
	blist = [n for c, n in bothlist if c == 'B']
    
	opos = bpos = 1
	bothidx = oidx = bidx = 0
	sec = 0
	while (bothidx != len(bothlist)):
		c, n = bothlist[bothidx]
		#print c, n, opos, bpos 
		#print (c == "O")
		if (c == "O" and n == opos):
			#O push button
			bothidx += 1
			oidx += 1
			#print "O push button"
		elif (oidx >= 0 and oidx < len(olist) and opos != olist[oidx]):
			opos += (opos - olist[oidx] > 0) and -1 or 1
			#print "O move:%d, %d" %(opos, olist[oidx])
			#O move
			
		if (c == 'B' and n == bpos):
			#B push button
			bothidx += 1
			bidx += 1
			#print "B push button"
		elif (bidx >= 0 and bidx < len(blist) and bpos != blist[bidx]):
			bpos += (bpos - blist[bidx] > 0) and -1 or 1
			#B move
			#print "B move:%d,%d" %(bpos, blist[bidx])
		sec += 1	
			
	#print "Seconds:%d" % (sec)
	print "Case #%d: %d" % (i+1, sec)
	#print bothlist, olist, blist
	
	