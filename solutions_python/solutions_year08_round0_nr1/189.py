#!/usr/bin/env python

data = open('A-large.in', 'rb')
result = open('A-large.out', 'wb')

n = int(data.readline())
for testCase in xrange(1, n+1):
    s = int(data.readline())
    engines = [data.readline() for i in xrange(s)]
    q = int(data.readline())
    queries = [data.readline() for i in xrange(q)]
    
    switches = dict((eng, 0) for eng in engines)
    for q in queries[::-1]:
        switches[q] = min(switches[eng] for eng in engines if q != eng) + 1
    
    result.write('Case #%i: %i\n' % (testCase, min(switches.itervalues())))

result.close()
data.close()
