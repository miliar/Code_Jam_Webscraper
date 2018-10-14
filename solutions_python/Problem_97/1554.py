#!/usr/bin/env python

#getting arguments
import sys
import getopt
usage = \
"""
Usage:
recycling.py -f file.inp
"""
if len(sys.argv)<3:
    print usage
    sys.exit()

opts, args = getopt.getopt(sys.argv[1:],"f:h:")
for o,a in opts:
    if o == "-h":
        print usage
        sys.exit()
    elif o == "-f": f=a
    else: print 'Invalid Option'

#Creating OUTPUT FILE
output=open('recycling.out','w')

#OPENING INPUT
count=0

for line in open(f):    
    if count>0:
        line=line.rstrip()
        a,b=line.split()
        moves  = len(str(a))-1
        counting=0
        output.write("Case #%d: "%count)
        if moves==0: output.write("0\n")
        else: 
            for n in range(int(a),int(b)+1):
                for j in range(1,moves+1):
                    x=str(n)[0:j]
                    y=str(n)[j:]
                    m=str(y)+str(x)
                    if (int(a)<=int(n)) and (int(n)<int(m)) and (int(m)<=int(b)):
                        counting+=1
            output.write("%d\n"%counting)
    count+=1
