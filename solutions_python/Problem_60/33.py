#!/usr/bin/env python2.6

#in_file = 'B-test.in'
#out_file = 'B-test.out'
#in_file = 'B-small-attempt0.in'
#out_file = 'B-small.out'
in_file = 'B-large.in'
out_file = 'B-large.out'

with open(in_file) as input:
    with open(out_file, 'w') as output:
        C = int(input.readline().rstrip())
        for c in range(1,C+1):
            sN,sK,sB,sT = input.readline().rstrip().split()
            N = int(sN)
            K = int(sK)
            B = int(sB)
            T = int(sT)

            locations = [int(l) for l in input.readline().split(None, N-1)]
            speeds = [int(l) for l in input.readline().split(None, N-1)]

            still_needed = K
            num_swaps = 0

            chick = N - 1
            while still_needed > 0 and chick >= 0:
                if (locations[chick] + (speeds[chick] * T)) < B:
                    num_swaps = num_swaps + still_needed
                else:
                    still_needed = still_needed - 1

                chick = chick - 1

            out = num_swaps
            if still_needed > 0:
                out = "IMPOSSIBLE"


            print >> output, 'Case #%d: %s' % (c,out)