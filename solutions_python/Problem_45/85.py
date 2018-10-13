#!/usr/bin/python

def readints(f):
    return map(lambda x: int(x), f.readline().strip().split(' '))

def perms(list):
    if list == []:
        return [[]]
    return [[list[i]] + p for i in range(len(list)) for p in perms(list[:i] + list[i+1:])]

def cost(l, P, Q):
    c = 0
    pr = [0] + [1 for _ in range(P)] + [0]
    while len(l) > 0:
        pr[l[0]] = 0
        i = l[0]+1
        while pr[i] == 1:
            c = c + 1
            i = i + 1
        i = l[0]-1
        while pr[i] == 1:
            c = c + 1
            i = i - 1
        l = l[1:]
    return c

if __name__ == '__main__':
    import sys
    inp = open(sys.argv[1], "r")

    
    [T] = readints(inp)
    for i in range(T):
        [P, Q] = readints(inp)
        R = readints(inp)
        minc = float('infinity')
        p = perms(R)
        for j in range(len(p)):
            if cost(p[j], P, Q) < minc:
                minc = cost(p[j], P, Q)
        print 'Case #%s: %d' % ((i+1), minc)
        
                                
