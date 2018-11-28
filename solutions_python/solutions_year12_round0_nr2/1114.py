#!/usr/bin/env python
# Karl WNW
# input stdin, output stdout

import sys

def check(n, p, diff=0):
    if diff > 4:
        return False, diff
    elif (p + p + p - diff) <= n:
        return True, diff
    else:
        return check(n, p, diff+1)

def how_many(i):
    l = map(int, sys.stdin.readline().split())

    #print l
    num = l.pop(0)
    s = l.pop(0)
    p = l.pop(0)

    count = 0


    for n in l:
        if n < p:
            continue

        isOk, diff = check(n, p)
        #print "s avant : %d" % s
        #print "score: %d" % n
        #print "isOk: ", isOk
        #print "diff: %d" % diff
    
        if isOk and diff >= 3:
            s -= 1

        if (isOk and diff < 3) or (isOk and s >= 0):
            count += 1

    print "Case #%d: %s" % (i, count)

def main():
    C = int(sys.stdin.readline().strip())
    for t in range(C):
        how_many(t+1)
    
if __name__ == '__main__':
    main()
