#!/usr/bin/python

megadict = {}

for n in range(1, 2000000):
    megadict[n] = set()
    s_n = str(n)
    for i in range(len(s_n)):
        m = int(s_n[i:] + s_n[:i])
        if n < m:
            megadict[n].add(m)

def solve():
    a, b = map(int, raw_input().split(' '))
    return sum(len(filter(lambda x: x <= b, megadict[i])) for i in range(a, b))

if __name__ == '__main__':
    T = int(raw_input())
    for case in xrange(1, T+1):
        print "Case #{0}: {1}".format(case, solve())
