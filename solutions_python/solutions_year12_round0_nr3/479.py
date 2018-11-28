#!/usr/bin/python3

from sys import argv

# recycled[n] contains all numbers m such that (n,m) is recycled pair n < m
# These numbers are not necessarily in any particular order
recycled = [[]]

for n in range(1, 2000001):
    recycled.append([])
    s = str(n)
    m = s
    while True:
        m = m[1:] + m[0]
        if m == s:
            break
        if m[0] != '0' and n < int(m):
            recycled[n].append(int(m))

infile= open(argv[1])
cases = int(infile.readline())
for i in range(cases):
    a, b = map(int, infile.readline().split())
    count = 0
    for n in range(a, b + 1):
        for m in recycled[n]:
            if a <= m <= b:
                count += 1
    print('Case #{}: {}'.format(i+1, count))
