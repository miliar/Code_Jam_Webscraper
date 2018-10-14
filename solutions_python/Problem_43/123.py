#!/usr/bin/python

def solve(s):
    n = len(set(list(s)))
    if n == 1:
        n = 2
    d = dict().fromkeys(set(list(s)))
    c = 0
    d[s[0]] = 1
    for i in range(len(s)):
        if d[s[i]] == None:
            d[s[i]] = c
            c = c+1
            if c == 1:
                c = 2
    p = 0
    for i in range(len(s)):
        p = p + d[s[i]]
        if i < len(s)-1:
            p = p * n
    return p

def readints(f):
    return map(lambda x: int(x), f.readline().strip().split(' '))

if __name__ == '__main__':
    import sys
    inp = open(sys.argv[1], "r")
    
    [N] = readints(inp)
    for i in range(N):
        s = inp.readline().strip()
        print 'Case #%s: %s' % ((i+1), solve(s))
        
                                
