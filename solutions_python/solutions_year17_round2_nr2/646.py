#! /usr/bin/python

import os
import sys
import copy

def debug(msg):
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        sys.stderr.write('%s' % msg)
        sys.stderr.write('\n')



        
def solve(N, R, O, Y, G, B, V):
    ret = []
    # case of two colors:
    if R == 0 and B == 0 and O == 0 and G == 0 and V == Y:
        return ''.join(['YV'] * V)
    if R == 0 and G == 0 and Y == 0 and V == 0 and B == O:
        return ''.join(['OB'] * B)
    if B == 0 and Y == 0 and V == 0 and O == 0 and R == G:
        return ''.join(['RG'] * B)
    #
    # place V
    yellows_first_replace = []
    if V > 0 and Y < V + 1:
        return 'IMPOSSIBLE'
    elif V > 0:
        yellows_first_replace.append('Y')
        yellows_first_replace += ['VY']*V
    # place O
    blue_first_replace = []
    if O > 0 and B < O + 1:
        return 'IMPOSSIBLE'
    elif O > 0:
        blue_first_replace.append('B')
        blue_first_replace += ['OB']*O
    # place G
    red_first_replace = []
    if G > 0 and R < G + 1:
        return 'IMPOSSIBLE'
    elif G > 0:
        red_first_replace.append('R')
        red_first_replace += ['GR']*O
    #
    debug('%s - %s - %s' % (yellows_first_replace, blue_first_replace, red_first_replace))
    #
    yellows = Y + (1 if yellows_first_replace else 0)
    blues = B + (1 if blue_first_replace else 0)
    reds = R + (1 if red_first_replace else 0)
    #
    # check if possible 
    if yellows > blues + reds:
        return 'IMPOSSIBLE'
    if blues > yellows + reds:
        return 'IMPOSSIBLE'
    if reds > yellows + blues:
        return 'IMPOSSIBLE'
    #
    # constract solution:
    ## create order : 
    unicorns_count = { 'Y': yellows, 'B': blues, 'R': reds }
    unicorns = list(reversed(sorted([
        (unicorns_count['Y'], 'Y'),
        (unicorns_count['B'], 'B'),
        (unicorns_count['R'], 'R')])))
    
    ## first place replacements
    prev = 'Q'
    first = None
    while True:
        if unicorns[0][0] == unicorns[1][0] == unicorns[2][0]:
            rest = []
            x1 = [x for x in ['B', 'Y', 'R'] if x != prev][0]
            rest.append(x1)
            x3 = [x for x in ['B', 'Y', 'R'] if x not in rest and x != first][0]
            rest.append(x3)
            x2 = [x for x in ['B', 'Y', 'R'] if x not in rest][0]
            debug('first = %s, prev = %s, x1 = %s, x2 = %s, x3 = %s' % (first, prev, x1,x2,x3))
            #
            ret += ('%s%s%s' % (x1, x2, x3)) * unicorns[0][0]
            return ''.join(ret)
        else:
            x = [x[1] for x in unicorns if x[1] != prev][0]
            debug ('choose x=%s' % x)
            if first is None:
                first = x
            prev = x
            ret.append(x)
            unicorns_count[x] -= 1
            unicorns = list(reversed(sorted([
                (unicorns_count['Y'], 'Y'),
                (unicorns_count['B'], 'B'),
                (unicorns_count['R'], 'R')])))

    
    # prev = 'Q'
    # if unicorns[0][0] > unicorns[1][0] and unicorns[1][0] > unicorns[2][0]:
    #     ret += [('%s%s' % (unicorns[0][1], unicorns[1][1]))] * unicorns[2][0]

        
    #     if yellows > 0 and yellows >= blues and yellows >= reds:
    #         yellows -= 1
    #         if yellows_first_replace:
    #             ret = ret + yellows_first_replace
    #             yellows_first_replace = None
    #         else:
    #             ret.append('Y')
    #     #
    #     elif blues > 0 and blues >= yellows and blues >= reds:
    #         blues -= 1
    #         if blue_first_replace:
    #             ret = ret + blue_first_replace
    #             blue_first_replace = None
    #         else:
    #             ret.append('B')
    #     #
    #     elif reds > 0 and reds >= yellows and reds >= blues:
    #         reds -= 1
    #         if red_first_replace:
    #             ret = ret + red_first_replace
    #             red_first_replace = None
    #         else:
    #             ret.append('R')
    #     else:
    #         raise Exception('?')
    #     #
    # return ''.join(ret)


T = int(sys.stdin.readline())
# For each test case
for t in range(1, T+1):
    debug(' ************* case %s' % t)
    [N, R, O, Y, G, B, V] = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    ret = solve(N, R, O, Y, G, B, V)
    sys.stdout.write('Case #%s: %s\n' % (t, ret))


