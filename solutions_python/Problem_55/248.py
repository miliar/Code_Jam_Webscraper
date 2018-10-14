#!/usr/bin/env python2.6

#in_file = 'ctest.in'
#out_file = 'ctest.out'
in_file = 'C-small.in'
out_file = 'C-small.out'
#in_file = 'C-large.in'
#out_file = 'C-large.out'

with open(in_file) as input:
    with open(out_file, 'w') as output:
        T = int(input.readline().rstrip())
        for t in range(1,T+1):
            R,k,N = [int(a) for a in input.readline().split(None, 2)]
            G = [int(a) for a in input.readline().split(None, N-1)]

            memo = {}

            if sum(G) <= k:
                answer = sum(G) * R
            else:
                answer = 0
                cur_front = 0
                next_r = R
                for r in range(0,R):
                    if memo.has_key(cur_front) and memo[cur_front][0] != r:
                        period_length = r - memo[cur_front][0]
                        period_money = answer - memo[cur_front][1]
                        runs_left = R - r
                        periods_possible = runs_left / period_length
                        answer += periods_possible * period_money
                        next_r = R-(runs_left%period_length)
                        break
                    load = 0
                    while load + G[cur_front] <= k:
                        load += G[cur_front]
                        cur_front = (cur_front + 1) % len(G)
                    answer += load

                    memo[cur_front] = (r+1, answer)

                for r in range(next_r, R):
                    load = 0
                    while load + G[cur_front] <= k:
                        load += G[cur_front]
                        cur_front = (cur_front + 1) % len(G)
                    answer += load

            print >> output, 'Case #%d: %d' % (t, answer)


