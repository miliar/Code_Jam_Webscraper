#!/usr/bin/env python
#
#

import re

name = 'A-large'
input_filename = '%s.in' % name
output_filename = '%s.out' % name
f = open(input_filename, 'r')

L, D, N = map(int, re.split('\s+', f.readline().strip()))
print 'L=%d, D=%d, N=%d' % (L, D, N)
print ''

aliens = [ f.readline().strip() for n in xrange(D) ]
patterns = [ f.readline().strip() for n in xrange(N) ]

from pprint import pprint
print('aliens:')
pprint(aliens)
print ''

print('patterns:')
pprint(patterns)
print ''

patterns = map(lambda v: v.replace('(','[').replace(')',']'), patterns)

print('patterns:')
pprint(patterns)
print ''

patterns = map(re.compile, patterns)

print('patterns:')
pprint(patterns)
print ''

fout = open(output_filename, 'w')
for i, pat in enumerate(patterns):
#    print i, pat.pattern
    count = 0
    for target in aliens:
        mo = pat.match(target)
        if mo:
            count += 1
    print 'Case #%d: %d' % (i+1, count)
    fout.write("Case #%d: %d\n" % (i+1, count))
