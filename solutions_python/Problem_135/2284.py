#! /usr/bin/env python
from sys import argv, maxint, exit

argc = len(argv)
if (argc < 2):
    print "NO FILE ARG"
    exit(1)

f = open(argv[1],'r')

T = int(f.readline())


for j in range(1,T+1):
    C1 = int(f.readline()) - 1
    layout1 = []
    layout1.append( f.readline().strip().split(' ') )
    layout1.append( f.readline().strip().split(' ') )
    layout1.append( f.readline().strip().split(' ') )
    layout1.append( f.readline().strip().split(' ') )

    C2 = int(f.readline()) - 1
    layout2 = []
    layout2.append( f.readline().strip().split(' ') )
    layout2.append( f.readline().strip().split(' ') )
    layout2.append( f.readline().strip().split(' ') )
    layout2.append( f.readline().strip().split(' ') )


    intersection = set(layout1[C1]) & set(layout2[C2])
    N = len(intersection)
    ans = None

    if (N == 1):
        ans = (j,intersection.pop())
    elif (N == 0):
        ans = (j,'Volunteer cheated!')
    else:
        ans = (j,'Bad magician!')
    print 'Case #%d: %s' % ans
