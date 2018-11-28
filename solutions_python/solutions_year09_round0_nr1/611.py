import re
import sys

L, D, N = map(int, sys.stdin.readline().split(' '))

words = [sys.stdin.readline().strip('\n') for i in xrange(D)]

patterns = [sys.stdin.readline().strip('\n') for i in xrange(N)]
patterns = map(lambda p: p.replace('(', '[').replace(')', ']'), patterns)

test = 1
for pattern in patterns:
    p = re.compile(pattern)
    matches = sum(map(lambda word: 1 if p.match(word) else 0, words))
    print 'Case #%d: %d' % (test, matches)
    test += 1
