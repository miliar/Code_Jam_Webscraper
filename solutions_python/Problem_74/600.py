#! /usr/bin/env python
#coding=utf-8

import sys
def main():
    if len(sys.argv) < 2:
        return
    
    f = open(sys.argv[1], "r").read().splitlines()
    t = int(f[0])
    for i in xrange(1, t + 1):
        z = f[i]
        s = z.split()
        n = int(s[0])
        time = 0
        robotmap = {"O": 0, "B": 1}
        posi = [1, 1]
        free = [0, 0]
        for j in xrange(n):
            r = robotmap[s[2 * j + 1]]
            b = int(s[2 * j + 2])
            mtime = abs(b - posi[r])
            #print mtime, free, time, 
            if mtime >= free[r]:
                mtime -= free[r]
                free[r] = 0
                free[1 - r] += mtime
                time += mtime
            else:
                free[r] = 0
            posi[r] = b
            free[1 - r] += 1
            time += 1
            #print mtime, free, time
        print "Case #%d: %d" % (i, time)

if __name__ == '__main__':
    main()