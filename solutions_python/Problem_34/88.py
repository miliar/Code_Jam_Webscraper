import re

f = open('alien_large.in')
(L,D,N) = map(int,f.readline().split())
words = [f.readline().strip() for _ in xrange(D)]
tests = [(f.readline().strip()).replace('(','[').replace(')',']') for _ in xrange(N)]
tests = map(re.compile,tests)

for (i,x) in enumerate(tests):
    print 'Case #%d:'%(i+1), sum([1 if x.match(y) else 0 for y in words ])

