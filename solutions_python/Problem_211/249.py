#! /usr/bin/python

import os
import sys
import copy
import operator

def debug(msg):
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        sys.stderr.write('%s' % msg)
        sys.stderr.write('\n')

def get_same_cores(cores):
    ret = 0
    value = cores[0]
    for i in range(len(cores)):
        if value == cores[i]:
            ret +=1
        else:
            return ret
    return len(cores)



def solve(cores_l, K, U):
    cores = sorted(cores_l)
    while U > 0.00000000001:
        debug('cores = %s (U=%s)' % (cores, U))
        same = get_same_cores(cores)
        if same >= len(cores):
            new_value = 1
            target_value_diff = 1 - cores[0]
        else:
            target_value_diff = (cores[same] - cores[0])
            new_value = cores[same]
        #
        value = cores[0]
        debug('cores = %s (U=%s, same=%s, target_value_diff=%s)' % (cores, U, same, target_value_diff))
        if same*target_value_diff <= U:
            for i in range(same):
                debug(' * adding to i=%s' % (i))
                cores[i] = new_value
            U -= target_value_diff * same
        else:
            i = 0
            for i in range(same):
                debug(' * adding to i=%s value: %s' % (i, U/same))
                cores[i] += U /same
            #if i < len(cores):
            #    debug(' * adding %s to %s' % (U, i))
            #    cores[i] += U
            #    U = 0
            break
    debug('last cores = %s (U=%s)' % (cores, U))
    return reduce(operator.mul, cores, 1)

sys.setrecursionlimit(15000)

T = int(sys.stdin.readline())
# For each test case
for t in range(1, T+1):
    debug(' ************* case %s' % t)
    [N, K] = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    U = float(sys.stdin.readline().strip())
    cores = [float(x) for x in sys.stdin.readline().strip().split(' ')]
    ret = solve(cores, K, U)
    debug('Case #%s: %.6f\n' % (t, ret))
    sys.stdout.write('Case #%s: %.6f\n' % (t, ret))
