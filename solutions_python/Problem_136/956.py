#! /usr/bin/python

import os, sys

def debug(msg):
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        sys.stderr.write(msg)
        sys.stderr.write('\n')

T = int(sys.stdin.readline())
input_data = {}
# For each test case
for t in range(1, T+1):
    debug("\n\n\n")
    [C, F, X] = [float(x) for x in sys.stdin.readline().split(' ')]
    doulbe_case = input_data.get((C, F, X))
    if doulbe_case is not None:
        ret = doulbe_case
    else:
        # tuple : fst is the cost after idx buys, snd is the cost to buy idx cookies
        #cost_per_buys = []
        #cost_per_buys[0] = (X/2, 0)
        prev_cost_to_buy_one_more = 0
        prev_cost_to_end = X/2
        i = 0
        debug("cost_to_buy_one_more, cost_to_end = (%s, %s)" % (prev_cost_to_buy_one_more, prev_cost_to_end))
        while True:
            debug("#### attempting one more buy")
            cost_to_buy_one_more = prev_cost_to_buy_one_more + C/(2.0 + i*F)
            cost_to_end = X / (2 + (i+1)*F)
            debug("cost_to_buy_one_more, cost_to_end = (%s, %s)" % (cost_to_buy_one_more, cost_to_end))
            if prev_cost_to_buy_one_more + prev_cost_to_end < cost_to_buy_one_more + cost_to_end:
                ret = prev_cost_to_buy_one_more + prev_cost_to_end
                break
            else:
                prev_cost_to_buy_one_more = cost_to_buy_one_more
                prev_cost_to_end = cost_to_end
                i += 1
    
        input_data[(C, F, X)] = ret
    sys.stdout.write('Case #%s: %.7f\n' % (t, ret))
