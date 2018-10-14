#!/usr/bin/env python2.7

import sys
import itertools

def max_above_p(n, surprise_ct , threshold, scores):
    max = 0

    possible_surprises = [i for i,s in enumerate(scores) if s > 1 and s < 29]
    surprise_combos = itertools.combinations(possible_surprises, surprise_ct)

    digests = [(s / 3, s % 3) for s in scores]
    print digests

    for sc in surprise_combos:
        print 'combo: ',
        print sc
        ct = 0
        #if m > 0 add 1 to avg for max
        #if surprise and m = 2 add 2
        #if surprise and m = 0 add 1
        for (i, (avg, m)) in enumerate(digests):
            surprise = i in sc
            if not surprise:
                if m > 0:
                    high = avg + 1
                else:
                    high = avg
            else:
                if m == 0:
                    high = avg + 1
                elif m == 1:
                    high = avg + 1
                elif m == 2:
                    high = avg + 2
            if high >= threshold:
                ct += 1
        max = ct if ct > max else max
    return max

input_file = open(sys.argv[1])

input_file.next()

outfile = open('dancers.out.txt','w') 
case = 0
for line in input_file:
    data = [int(i) for i in line.strip().split(' ')]
    (n, s, p) = data[:3]
    totals = data[3:]

    #print n, s, p
    #for tot in totals: print tot,
    
    #print
   
    max = max_above_p(n, s, p, totals)
    case += 1
    outfile.write('Case #%d: %d\n' % (case, max))
