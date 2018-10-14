#!/usr/bin/env python
# Karl WNW
# input stdin, output stdout

import sys
from collections import deque

def how_many(i):
    l = map(int,sys.stdin.readline().split())
    count = 0
    recycled_pairs = []

    for n in xrange(l[0], l[1]+1):
        s = deque(str(n))
        currentInt = int(''.join(s))
        
        if len(s) > 1:
            # do not rotate numbers that won't change (22, 1111, ...)
            if not s.count(s[0]) == len(s):
                for c in range(len(s)-1):
                    s.rotate(1)
                    newInt = int(''.join(s))

                    if newInt <= l[1] and \
                       newInt >= l[0] and \
                       newInt != currentInt and \
                       not (sorted([newInt, currentInt]) in recycled_pairs):

                        recycled_pairs.append(sorted([currentInt, newInt]))
                        count += 1

    print "Case #%d: %s" % (i, count)

def main():
    C = int(sys.stdin.readline().strip())
    for t in range(C):
        how_many(t+1)
    
if __name__ == '__main__':
    main()
