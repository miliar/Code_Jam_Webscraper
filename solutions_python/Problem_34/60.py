import sys
import re

f = sys.stdin

L, D, N = map(int, next(f).split())
words = [next(f).strip() for i in range(D)]
for X, line in enumerate(f, 1):
    line = line.strip().replace('(', '[').replace(')', ']')
    patt = re.compile(line)
    K = sum(bool(patt.match(word)) for word in words)
    print 'Case #%d: %d' % (X, K)
