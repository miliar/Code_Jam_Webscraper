#! /usr/bin/python

import os, sys, copy

def debug(msg):
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        sys.stderr.write('%s' % msg)
        sys.stderr.write('\n')

T = int(sys.stdin.readline())
for t in range(1, T+1):
    [smax, s_list] = sys.stdin.readline().strip().split(' ')
    debug('smax = <%s>' % smax)
    debug('slist = <%s>' % s_list)
    count = 0
    solve = 0
    for needed, s in enumerate(s_list):
        debug('s = %s, count = %s, needed = %s' % (s, count, needed))
        if needed > count:
            solve += (needed - count)
            count += (needed - count)
        count += int(s)
        debug(' * solve = %s' % solve)
    sys.stdout.write('Case #%s: %s\n' % (t, solve))
