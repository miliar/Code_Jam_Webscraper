#! /usr/bin/python

import sys
import math

if len(sys.argv) < 3:
	exit(1)

finname = sys.argv[1]
foutname = sys.argv[2]

print "{} {}".format(finname,foutname)

fin=open(finname,"r")
fout=open(foutname,"w")

numcases=int(fin.readline());

print numcases

for case in range(0,numcases):
    fout.write ("Case #%d: " % (case+1))
    line=fin.readline()
    line=line.split()
    r=int(line.pop(0))
    c=int(line.pop(0))
    w=int(line.pop(0))

    print "r: %d, w: %d, c: %d" % (r,w,c)

    if (c == w):
        print "sol: %d" % (w)
        sol=w
    else:
        div=int(c/w)
        if(0 == c%w):
            div=div-1
        sol=div+w
        print "sol: %d" % (sol)
    fout.write ("%d\n" % (sol))

#	print "%d %d" % (sum1, sum2)
#	fout.write("%d %d\n" % (sum1, sum2) )
			



