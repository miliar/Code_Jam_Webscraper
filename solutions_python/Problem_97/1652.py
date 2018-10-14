#!/usr/bin/env python

def rot_match ( A, B, n ):
    str_A, str_B = map(str, (A,B))
    rot_A = str_A[n:] + str_A[:n]
    #if rot_A == str_B:
        #print "(%s,%s) || %s" % (A,B, rot_A)
    return rot_A == str_B

def solve ( n ):
    print "Case #%s: " % n,
    rawline = raw_input()
    splitline = rawline.split(" ")
    A,B = map(int, splitline)
    pairs = set()
    for x in xrange(A,B):
        for y in xrange(x+1,B+1):
            len_x, len_y = map(len, map(str, (x,y)))
            if len_x == len_y:
                for i in xrange(1, len_x):
                    if rot_match(x, y, i):
                        pairs.add((x,y))
    print len(pairs)

if __name__ == "__main__":
    T = input()
    for n in xrange(1, T+1):
        solve(n)

