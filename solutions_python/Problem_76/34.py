#!/usr/bin/python

import sys

def candy(arr):
    total = 0
    for x in arr:
        total = total ^ x
    if total != 0:
        return "NO"
    else:
        return str(sum(arr)-min(arr))

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if not len(argv) == 2:
        print >>sys.stderr, "Usage: store-credit.py infile"

    infile = argv[1]
    f = open(infile, 'r')
    N = int(f.readline())

    for i in range(N):
        f.readline()
        arr = map(lambda x: int(x), f.readline().strip().split())
        result = candy(arr)
        print "Case #%d: %s" % (i + 1, result)
        
if __name__ == "__main__":
    sys.exit(main())

