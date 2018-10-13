import re

L, D, N = map(int, raw_input().split())

words = []
for i in xrange(D):
    words.append(raw_input())

for i in xrange(N):
    test = raw_input()
    test = test.replace('(', '[')
    test = test.replace(')', ']')
    test = re.compile(test)
    print 'Case #%d: %s' % (i+1, len(test.findall('\n'.join(words))))
