import sys

sys.stdin = open('B-small-attempt0.in', 'r')
# sys.stdin = open('B-large.in', 'r')
sys.stdout = open('b-small.out', 'w')
# sys.stdout = open('b-large.out', 'w')

def solution(c, j):
    x = c.count('?') + j.count('?')
    r = c + ' ' + j
    y = list(r)
    import itertools
    import math
    m = 9999
    res = [] 
    for k in list(itertools.product([0,1,2,3,4, 5, 6, 7, 8, 9],repeat=x)):
        import copy
        t = copy.deepcopy(y)
        for n in k:
            t[t.index('?')] = str(n)
        s = ''.join(t)
        a = int(s.split()[0])
        aa = s.split()[0]
        bb = s.split()[1]
        b = int(s.split()[1])
        if m > abs(a-b):
            res = [[aa, bb]]
            m = abs(a-b)
        elif m == abs(a-b):
            res.append([aa,bb])
        else:
            continue
    c, j = res[0]
    return c, j

for t in range(int(input())):
    c, j = raw_input().split()
    c, j = solution(c, j)
    
    print 'Case #%d: %s' % (t + 1, '%s %s' % (c, j))
