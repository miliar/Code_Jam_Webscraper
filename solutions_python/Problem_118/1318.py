#!/usr/bin/python

import sys
import math


def ReadN(fp):
    return int(fp.readline().strip())


def ReadAB(fp):
    return [int(t) for t in fp.readline().strip().split()]


def IsFair(t):
    st = str(t)
    N = len(st)
    for i in xrange(int(math.floor(N/2))):
        if st[i]!=st[N-1-i]:
            return False
    return True

def CountAB(A,B):
    cnt = 0
    ta = int(math.floor(math.sqrt(A)))
    tb = int(math.ceil(math.sqrt(B)))
    for t in xrange(ta,tb+1):
        t2 = t * t
        if t2 < A:
            continue
        elif t2 > B:
            break
        else:
            if IsFair(t2) and IsFair(t):
        #        print t2
                cnt = cnt +1
    return cnt


#cnt = CountAB(1, 4)
cnt = CountAB(100, 1000)


def Test(fname):
    fp = open(fname)
    res = open(fname[:-3]+"_res.txt","wt")
    N = ReadN(fp)
    for i in xrange(N):
        [A, B] = ReadAB(fp)
        cnt = CountAB(A, B)
        ans = "Case #%d: %d\n" %(i+1,cnt)
        print ans,
        res.write(ans)
    print "done."


if __name__=="__main__":
    if len(sys.argv)<2:
        print "please give the input file"
        sys.exit()
    fname = sys.argv[1]
    Test(fname)

