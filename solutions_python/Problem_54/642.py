'''
Created on 2010/05/08
@author: aflc
'''

import sys

def gcd(a, b):
    s, l = sorted((a, b))
    rem = 1
    while s > 0:
        l, (div, s) = s, divmod(l, s)
    return l

with open(sys.argv[1], 'r') as fi:
    with open('out.txt', 'w') as fo:
        num = 0
        for s in fi:
            evtscnds = s.strip().split(' ')
            if len(evtscnds) > 1:
                num += 1
                print num
                evtscnds = map(int, evtscnds[1:])
                evtscnds.sort()
                subs = [evtscnds[i + 1] - evtscnds[i] for i in range(len(evtscnds) - 1)]
                subs = filter(lambda x: x != 0, subs)
                gcdn = reduce(gcd, subs)
                rem = divmod(evtscnds[0], gcdn)[1]
                res = 0 # if rem = 0
                if rem > 0:
                    res = gcdn - rem
                fo.write('Case #' + str(num) + ': ' + str(res) + '\n')




