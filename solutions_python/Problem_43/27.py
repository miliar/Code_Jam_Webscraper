#! /usr/bin/python
# -*- coding:utf-8

import sys

def geta(S):

    a = set()
    for i in range(0,len(S)):
        a.add(S[i])
    d = {}
    s = [0]*len(S)
    if len(S) == 1:
        return 1

    d[S[0]] = 1

    A=[0] + range(2,30)

    s[0] = 1
    cur = 0
    for i in range(1,len(S)):
        try:
            s[i] = d[S[i]]
        except:
            d[S[i]] = A[cur]
            cur += 1
            s[i] = d[S[i]]

    b = max(2,len(a))
    res = 0
    r = 1
    for i in range(len(s)):
        c = s[len(s)-1-i]
        res += c*r
        r *= b

    return res

def main( file ):
    f = open( file )
    T = int( f.readline().strip() )
    for t in range(T):
        S = f.readline().strip()
        print "Case #%d: %d" % (t + 1, geta(S) )
        #print "\n".join( [ " ".join( ans[y] ) for y in range(len(ans)) ] )
        
if __name__ == '__main__': main(sys.argv[1])

