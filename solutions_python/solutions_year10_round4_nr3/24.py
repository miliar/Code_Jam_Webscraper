################################################################
size = 100

def solve():
    (R,) = [int(x) for x in input.readline().split(' ')]
    RS = [[int(x) for x in input.readline().split(' ')] for i in range(0,R)]
    rect = [[0 for i in range(0,size)] for i in range(0,size)]
    for (X1,Y1,X2,Y2) in RS:
        for x in xrange(X1-1,X2):
            for y in xrange(Y1-1,Y2):
                rect[x][y] = 1
    def runround():
        any = False
        prev_x = [0 for i in range(0,size)]
        prev_y = 0
        def loc(x,y):
            if x<0 or y<0: return 0
            else: return rect[x][y]
        for x in range(0,size):
            for y in range(0,size):
                prev = loc(x,y)
                any = any or prev
                n = prev_y
                w = prev_x[y]
                if n==0 and w==0: next = 0
                elif n==1 and w==1: next = 1
                else: next = rect[x][y]
                prev_y = rect[x][y]
                prev_x[y] = rect[x][y]
                rect[x][y] = next
        return any
    rounds = 0
    while (runround()):
        rounds +=1
    return rounds
################################################################

from datetime import datetime
time_start = datetime.today()
def now(): return datetime.today() - time_start 

import sys
infilename = sys.argv[1]
outfilename = infilename.replace('.in','.out')

input = open(sys.argv[1], 'r')
output = open(sys.argv[1].replace('.in','.out'), 'w')
n = int(input.readline())

for i in range(1,n+1):
    result = solve()
    print "Case #%d: %d \t %s" % (i, result, now())
    output.write("Case #%d: %d\n" % (i, result))
