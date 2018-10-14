#!/usr/bin/python


def read():
    res = []
    with open('A.in', 'r') as f:
        t = int(f.readline())
        for _ in xrange(t):
            d, n = map(int, f.readline().split())
            k, m = [], []
            for _ in xrange(n):
                ki, mi = map(int, f.readline().split())
                k.append(ki)
                m.append(mi)
            res.append([d, k, m])
    return res


def solve(d, k, s):
    maxx = -1
    maxi = None
    for i in xrange(len(k)):
        if (d-k[i])/float(s[i]) > maxx:
            maxx = (d-k[i])/float(s[i])
            maxi = i
    return d/maxx


def write():
    data = read()
    with open('A.out', 'w') as f:
        for i, d in enumerate(data):
            f.write('Case #%d: %f\n' % ((i + 1), solve(d[0], d[1], d[2])))



'''
print solve(2525, [2400], [5])
print solve(300, [120, 60], [60, 90])
print solve(100, [80, 70], [100, 10])
'''
write()
