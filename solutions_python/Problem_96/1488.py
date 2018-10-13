#!/usr/bin/env python3
import sys

debug = print
debug = lambda msg: None

for i, line in enumerate(sys.stdin):
    if i == 0:
        continue
    numbers = list(map(int, line.split(' ')))
    
    N_googlers, S_suprising, p_at_least = numbers[0:3]
    points = numbers[3:]
    
    # debug('Case #%d: %d googlers: %r' % (i, N_googlers, points))
    
    points.sort(reverse=True)
    
    debug("after sorting: %r" % (points))
    
    num_above_limit = 0
    for pt in points:
        debug('-- %d:' % pt)
        if pt / 3 >= p_at_least:
            num_above_limit += 1
            debug('    is above limit of %r' % (p_at_least))
            continue
        judge_1 = p_at_least
        left = pt - p_at_least
        
        if left < 0:
            break
        
        judge_2 = left // 2       # the smaller one
        judge_3 = left - judge_2  # the bigger one of the two
        
        debug('    judges: %r' % ((judge_1, judge_2, judge_3),))
        
        if judge_2 > (judge_1 - 2):
            num_above_limit += 1
            continue
        
        if judge_2 == (judge_1 - 2) and S_suprising:
            S_suprising -= 1
            num_above_limit += 1
            continue
        
        # else: no suprising left and difference too big, break here...
        break
    
    debug('-- Case #%d: %d\n' % (i, num_above_limit))
    print('Case #%d: %d' % (i, num_above_limit))
