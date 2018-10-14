#! /usr/bin/env python
# vim: set et ts=4 sw=4 ci cino=(0:
import sys
import os


def strdiffer( old, new ):
    for i in xrange(len(new)):
        if len(old) <= i or old[i] != new[i]:
            return i
    print "Error  Error"
    sys.exit(1)

def main():
    f = open(sys.argv[1])
    ntest = int(f.readline().strip())


    for k in xrange(ntest):
        l = [ int(x) for x in f.readline().strip().split() ]
        n = l[0]
        m = l[1]

        paths = []
    
        for j in xrange(n):
            l = f.readline().strip()
            paths.append((l + "/",False))
        
        for j in xrange(m):
            l = f.readline().strip()
            paths.append((l + "/",True))
        paths.sort()

        lastpath = "/"
        count = 0
        for i in xrange(len(paths)):
            npath = paths[i][0]
            if paths[i][1] == True and npath != lastpath:
                locdiff = strdiffer( lastpath, npath )
                for x in xrange(locdiff, len(npath)):
                    if npath[x] == "/":
                        count = count + 1
            lastpath = npath
        print "Case #%d: %d" % (k+1, count )

if __name__ == "__main__":
    main()

