#!/usr/bin/env python2.6

in_file = 'btest.in'
out_file = 'btest.out'
in_file = 'B-small.in'
out_file = 'B-small.out'
in_file = 'B-large.in'
out_file = 'B-large.out'

def gcd(a, b):
    if a < b:
        tmp  = a
        a = b
        b = tmp
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a

with open(in_file) as input:
    with open(out_file, 'w') as output:
        C = int(input.readline().rstrip())
        for c in range(1,C+1):
            line = input.readline().rstrip()
            N , rest = line.split(None, 1)
            T = [int(a) for a in rest.split(None, int(N)-1)]
            tot_set = set()
            for t1 in T:
                for t2 in T:
                    diff = abs(t1 -t2)
                    if diff != 0:
                        tot_set.add(diff)

            diffs = list(tot_set)
            gcd_t = diffs.pop()
            while len(diffs) > 0:
                gcd_t = gcd(gcd_t, diffs.pop())

            answer = gcd_t - (min(T) % gcd_t)
            if answer == gcd_t:
                answer = 0

            print >> output, 'Case #%d: %d' % (c, answer)

            
            



