#!/usr/bin/env python

#getting arguments
import sys
import getopt
usage = \
"""
Usage:
fsq.py -f file.inp -o file.out
"""
if len(sys.argv)<5:
    print usage
    sys.exit()

opts, args = getopt.getopt(sys.argv[1:],"f:o:h:")
for o,a in opts:
    if o == "-h":
        print usage
        sys.exit()
    elif o == "-f": f=a
    elif o == "-o": o=a
    else: print 'Invalid Option'

# OPENING INPUT

lines=[]
for line in open(f):
    line=line.rstrip()
    temp=line.split()
    lines.append(temp)

# CREATING OUTPUT FILE
output=open(o,'w')

for i in range(1,int(lines[0][0])+1):
    output.write("Case #%d: "%i)
    squares=[]
    number=[]
    x=0
    count=0

    while x<=int(lines[i][1]):
        if (x*x>=int(lines[i][0])) and (x*x<=int(lines[i][1])): 
            squares.append(x*x)
            number.append(x)
        x+=1

    for j in range(len(squares)):

        a=str(squares[j])
        a1=str(number[j])
        c=len(a)-1
        c1=len(a1)-1
        b=''
        b1=''

        while c>=0:
            b+=str(a[c])
            c-=1
        while c1>=0:
            b1+=str(a1[c1])
            c1-=1

        if (str(b)==str(a)) and (str(b1)==str(a1)): 
            count+=1
        
    output.write("%d\n"%count)
        
            
    
         




