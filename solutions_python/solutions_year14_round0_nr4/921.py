#! /usr/bin/python

import os, sys, copy

def debug(msg):
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        sys.stderr.write('%s' % msg)
        sys.stderr.write('\n')

T = int(sys.stdin.readline())
input_data = {}
# For each test case
for t in range(1, T+1):
    debug('#'*70)
    debug("\n\n\n")
    num = int(sys.stdin.readline())
    naomi = sorted([float(x) for x in sys.stdin.readline().split(' ')])
    ken = (sorted([float(x) for x in sys.stdin.readline().split(' ')]))
    #
    debug(naomi)
    debug(ken)
    debug('#'*20)
    war_points = 0
    d_war_points = 0
    ken_list = ken
    d_ken_list = ken
    d_ken_start = 0
    d_ken_end = len(ken)
    for i in range(0, num):
        naomi_value = naomi[i]
        debug('naomi %s' % naomi_value)
        debug(ken_list)
        if naomi_value > ken_list[0]:
            found = False
            for j, v in enumerate(ken_list):
                if v > naomi_value:
                    debug('found')
                    found = True
                    ken_list = ken_list[0:j] + ken_list[j+1:]
                    break
            if not found:
                war_points += 1
        else:
            ken_list = ken_list[1:]
        # new war
        if naomi_value > d_ken_list[d_ken_start]:
            d_ken_start += 1
            d_war_points += 1
        elif naomi_value < d_ken_list[d_ken_end - 1]:
            d_ken_end -= 1
                
        
    sys.stdout.write('Case #%s: %s %s\n' % (t, d_war_points, war_points))
