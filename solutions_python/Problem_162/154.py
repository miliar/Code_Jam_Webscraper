#!/usr/bin/python
import sys
basename, = sys.argv[1:]
input_filename = basename + ".in"
output_filename = basename + ".out"
input = open(input_filename)
output = open(output_filename, 'w')
print 'writing to', output_filename

T = int(input.readline())

def reverse(n):
    l = list(str(n))
    l.reverse()
    return int(''.join(l))

assert reverse(643) == 346
assert reverse(1030) == 301

d = {1: 1}
first = 1

def good(N):
    global d
    global first
    
    d[1] = 1
    while not N in d:
        if first % 100000 == 0:
            print first
        v = d[first]+1
        for n in (first+1, reverse(first)):
            d[n] = min(d.get(n, v), v)
        first += 1
    return d[N]

def dist(n):
    if n<20:
        return n
    if n % 10 == 0:
        return 1 + dist(n-1)
    count = 0
    s = str(n)
    l = len(s)
    k = l // 2
    d = int(s[k:l])-1
    n -= d
    count += d
    assert n % 10 == 1
    nn = reverse(n)
    if nn != n:
        count += 1
    n = nn
    d = int(str(n)[1:]) + 1
    n -= d
    count += d
    return count + dist(n)

def solve():
    global first
    N = int(input.readline())
    return dist(N)

for t in range(T):
    print >> output, 'Case #%s: %s' % (t+1,solve())
