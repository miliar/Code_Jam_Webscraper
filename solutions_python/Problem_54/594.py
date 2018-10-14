#!/usr/bin/env python
# Sreenath Are, 2010

from fractions import gcd

(lambda f:f.write((lambda l: '\n'.join(l[i] and 'Case #{0}: {1}'.format(i+1,(lambda l: -l[0]%reduce(gcd,(abs(l[i]-l[i+1]) for i in xrange(len(l)-1))))(l[i])) or '' for i in xrange(len(l))))([map(int,i.split()[1:]) for i in open('warning.in').read().split('\n')[1:]])) and f.close())(open('warning.out','w'))
