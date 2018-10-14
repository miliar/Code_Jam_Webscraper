#!/usr/bin/python

def readints(f):
    return map(lambda x: int(x), f.readline().strip().split(' '))

def tree(s):
    nums = [str(x) for x in range(10)] + ['.']
    T = dict()
    
    i = 1
    v = ''
    while s[i] in nums:
        v = v + s[i]
        i = i + 1

    T['v'] = float(v)
    s = s[i:]

    if s[0] == ')':
        T['f'] = None
        T['l'] = None
        T['r'] = None
    else:
        i = 0
        f = ''
        while s[i] != '(':
            f = f + s[i]
            i = i + 1
        T['f'] = f
        s = s[i:]
        (T['l'], s) = tree(s)
        (T['r'], s) = tree(s)
    s = s[1:]
    
    return (T, s)

def decision(T, C, p):
    p = p*T['v']
    if T['f'] == None:
        return p
    else:
        if T['f'] in C:
            return decision(T['l'], C, p)
        else:
            return decision(T['r'], C, p)

def readints(f):
    return map(lambda x: int(x), f.readline().strip().split(' '))

if __name__ == '__main__':
    import sys
    inp = open(sys.argv[1], "r")
    [N] = readints(inp)
    for i in range(N):
        [L] = readints(inp)
        t = ''
        for j in range(L):
            t = t + inp.readline().strip()
        (T, s) = tree(t.replace(' ', ''))

        [A] = readints(inp)
        print 'Case #%s:' % (i+1)
        for j in range(A):
            S = inp.readline().strip().split(' ')
            print '%.10f' % (decision(T, set(S[2:]), 1))
