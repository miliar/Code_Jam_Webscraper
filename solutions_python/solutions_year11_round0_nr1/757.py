#! /usr/bin/env python2

import sys

def check_target(ct, pos, tg):
    if not tg:
        return False, ct
    (id, tgpos) = tg[0]
    if pos == tgpos and id == ct:
        tg.pop(0)
        return True, ct + 1
    return False, ct

def solve(targets, ntargets):
    curr_target = 0
    elapsed_time = 0
    b_pos = 1
    o_pos = 1
    while curr_target < ntargets:
        b_done, o_done = False, False

        b_done, curr_target = check_target(curr_target, b_pos, targets['B'])
        if not b_done:
            o_done, curr_target = check_target(curr_target, o_pos, targets['O'])

        if not b_done and targets['B']:
            tgpos = targets['B'][0][1]
            if b_pos > tgpos:
                b_pos -= 1
            elif b_pos < tgpos:
                b_pos += 1

        if not o_done and targets['O']:
            tgpos = targets['O'][0][1]
            if o_pos > tgpos:
                o_pos -= 1
            elif o_pos < tgpos:
                o_pos += 1

        elapsed_time += 1
        b_done, o_done = False, False

    return elapsed_time

if __name__ == '__main__':
    T = input()
    for t in xrange(T):
        print >>sys.stderr, 'Case #%d started' % (t + 1)
        fields = raw_input().split()[1:]
        targets = { 'B': [], 'O': [] }
        for i in xrange(0, len(fields), 2):
            targets[fields[i]].append((i / 2, int(fields[i + 1])))
        print 'Case #%d: %d' % (t + 1, solve(targets, len(fields) / 2))
