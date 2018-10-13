#!/usr/bin/env python

key = "welcome to code jam"
kl = len(key)
md = 100000000
kpos = []
c = 0
l = ''

def searchkey(idx):
    global c, l, kpos
    if idx >= kl:
        c += 1
        if c > md:
            c %= 10000
        return True

    found1 = False
    while kpos[idx] < len(l):
        np = l.find(key[idx], kpos[idx])
        if np == -1:
            return found1
        
        kpos[idx] = np
        kpos[idx + 1] = np + 1
#        print idx, kpos[idx]
        if ( not searchkey(idx + 1) ):
            return found1
        else:
            found1 = True
            kpos[idx] += 1

    return found1


def solve_case(fin):
    global c, l, kpos
    l = fin.readline()
    c = 0
    kpos = [kl + 10] * (kl + 1)
    kpos[0] = 0
    searchkey(0)
    c %= 10000
    return '{0:04d}'.format(c)


def solve(fin):
    n = int(fin.readline())
    for i in range(n):
        out = solve_case(fin)
        print 'Case #{0}: {1}'.format(i+1, out)

def main():
    import sys
    solve(sys.stdin)

if __name__ == '__main__':
    main()
