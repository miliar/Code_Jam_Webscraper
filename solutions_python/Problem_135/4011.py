#!/usr/bin/python
import sys
from pprint import pprint


BAD='Bad magician!'
CHEATED='Volunteer cheated!'


def debug(s,*args):
    argstr = map( str, args)
    sys.stderr.write(s+' '+' '.join(argstr)+'\n')

debug('opening',sys.argv[1])
f = open(sys.argv[1])


T = int(f.readline().strip())

#while f:
    #print '--',f.readline(),'--'

def read_quad(f):
    rows = []
    for i in range(4):
        line = f.readline()
        rows.append(set(map(int,line.split())))
    return rows

#for line in f.readlines(f):
case = 1
while case <= T:
    n1 = int(f.readline())
    quad1 = read_quad(f)
    n2 = int(f.readline())
    quad2 = read_quad(f)

    row1 = quad1[n1-1]
    row2 = quad2[n2-1]
    diff = row1.intersection(row2)

    if len(diff) == 0:
        result = CHEATED
    elif len(diff) == 1:
        result = str(diff.pop())
    else:
        result = BAD
    
    print "Case #{}: {}".format(case,result)

    #pprint(quad1)
    #print row2
    #pprint(quad2)

    case += 1


