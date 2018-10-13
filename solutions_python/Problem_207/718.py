import sys
#from heapq import *
sys.stdin  = open('input.in', 'r')
sys.stdout = open('output.txt', 'w')

test = input()
for _ in xrange(1,test+1):
    print 'Case #' + str(_) + ':',
    n,r,o,y,g,b,v = map(int,raw_input().split())
    a = [[r,'R'],[y,'Y'],[b,'B']]
    a.sort()
    if a[2][0] > a[1][0] + a[0][0] :
        print "IMPOSSIBLE"
        continue
    ans = ''
    while a[2][0] != a[1][0] + a[0][0] :
        ans = ans + a[2][1] + a[1][1] + a[0][1]
        a[2][0] -= 1;a[1][0] -= 1;a[0][0] -= 1
    while a[1][0] != 0:
        ans = ans + a[2][1] + a[1][1]
        a[1][0] -= 1
    while a[0][0] != 0:
        ans = ans + a[2][1] + a[0][1]
        a[0][0] -= 1
    print ans