#!/usr/bin/env python2.6

#in_file = 'test.in'
#out_file = 'test.out'
#in_file = 'A-small.in'
#out_file = 'A-small.out'
in_file = 'A-large.in'
out_file = 'A-large.out'

with open(in_file) as input:
    with open(out_file, 'w') as output:
        T = int(input.readline().rstrip())
        for t in range(1,T+1):
            n,k = [int(a) for a in input.readline().split(None, 1)]
            status = sum([int((k)/(2**(a-1))) % 2 for a in range(1, n+1) ])
            str_status = 'OFF'
            if status == n:
                str_status = 'ON'
            print >> output, 'Case #%d: %s' % (t,str_status)
