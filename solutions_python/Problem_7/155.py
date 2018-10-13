#!/usr/bin/python
import sys

def numbers(n,A,B,C,D,x0,y0):
    X = x0
    Y = y0
    yield (X, Y)
    for i in range(n-1):
        X = (A * X + B) % M
        Y = (C * Y + D) %M
        yield X, Y

if __name__ == "__main__":
    i = int(sys.stdin.readline())
    for c in range(i):
        n, A, B, C, D, x0, y0 , M = map(int,sys.stdin.readline().split())
        nums = set()
        sums = set()
        for a,b in numbers(n,A,B,C,D,x0,y0):
                nums.add((a,b))
                sums.add((a * 3, b *3))
        #        print a,b
        count = 0 
        l = list(nums)
        #print l 
        #print sums
        for i1, (x1,y1) in enumerate(l):
            #print l[i1 + 1:] 
            for i2, (x2,y2) in enumerate(l[i1 + 1:]):
                #print l[i1 + i2 +2:]
                for x3,y3 in l[i1 + i2 + 2:]:
                   #print `(x1,y1)` + "," + `(x2,y2)` + `(x3,y3)` 
                   if (x1+x2+x3) %3 == 0 and (y1+y2+y3) % 3 == 0:
                       count = count + 1

        print "Case #%d: %d" % (c + 1,count)

