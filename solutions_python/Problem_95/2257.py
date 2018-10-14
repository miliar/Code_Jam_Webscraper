#!/usr/bin/env python




def do(seq):


##    'seq='de kr kd eoya kw aej tysr re ujdr lkgc jv'

    ##seq='rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
    ##seq='ejp mysljylc kd kxveddknmc re jsicpdrysi'
    ##seq='mneicwlb'
    output=[]
    x=list(' abcdefghijklmnopqrstuvwxyz')
    y=list(' ynficwlbkuomxsevzpdrjgthaq')

    ##print x.index('c')

    for i in xrange(len(seq)):
    ##    print seq[i]
        output.append(x[y.index(seq[i])])

    print 'output',''.join(output)
    return ''.join(output)

##print 'the end'
##sys.exit(0)

import sys
fname=sys.argv[1]

print 'fname',fname
input=[]
f=open(fname+'','r')
fout=open(fname+'.out','w')
numLine=int(f.readline())
for num in xrange(1,numLine+1):
    line=f.readline().strip()

    print 'Case #'+`num`+': '+do(line)
    fout.write('Case #'+`num`+': '+do(line)+'\n')
fout.close()

