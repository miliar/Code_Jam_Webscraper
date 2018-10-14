#! /usr/bin/env python
# vim: set et ts=4 sw=4 ci cino=(0:
import sys
import os


def findsubstr( h, v, da, sub ):
    for i in xrange(len(h)):
        if h[i].find(sub) != -1:
            return True

    for i in xrange(len(v)):
        if v[i].find(sub) != -1:
            return True

    for i in xrange(len(da)):
        if da[i].find(sub) != -1:
            return True

    return False


def main():
    f = open(sys.argv[1])
    ntest = int(f.readline().strip())


    for i in xrange(ntest):
        foundB = False
        foundR = False

        l = [ int(x) for x in f.readline().strip().split() ]
        n = l[0]
        k = l[1]
        v = []
        for j in xrange(n):
            l = f.readline().strip()
            sl = [ x for x in l[::-1] if x != "." ]
            sls = "".join(sl)
            sls = sls + ('.' * (n - len(sls)))
            v.append(sls)

        h = []
        for j in xrange(n):
            h.append("".join([ t[j] for t in v ]))

        da = []
        for j in xrange(k-1,n):
            tl = []
            ib = j
            for ia in xrange(j+1):
                tl.append( v[ia][ib] )
                ib = ib - 1
            da.append("".join(tl))

        for j in xrange(k-1,n):
            tl = []
            ib = j
            for ia in xrange(j+1):
                tl.append( v[ia][::-1][ib] )
                ib = ib - 1
            da.append("".join(tl))

        for j in xrange(k-1,n):
            tl = []
            ib = j
            for ia in xrange(j+1):
                tl.append( h[ia][ib] )
                ib = ib - 1
            da.append("".join(tl))

        for j in xrange(k-1,n):
            tl = []
            ib = j
            for ia in xrange(j+1):
                tl.append( h[ia][::-1][ib] )
                ib = ib - 1
            da.append("".join(tl))


        bstr = 'B' * k
        rstr = 'R' * k
        if findsubstr( h, v, da, bstr ):
            foundB = True
        if findsubstr( h, v, da, rstr ):
            foundR = True

        ans=""
        if foundB and foundR:
            ans = "Both"
        elif foundB and (not foundR):
            ans = "Blue"
        elif (not foundB) and foundR:
            ans = "Red"
        else:
            ans = "Neither"

        print "Case #%d: %s" % (i+1, ans )

if __name__ == "__main__":
    main()

