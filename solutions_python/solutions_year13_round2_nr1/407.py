#!/usr/bin/python

import sys

num_cases = int(sys.stdin.readline())
for case in range(1, num_cases + 1):
    armins_mote = int(sys.stdin.readline().split()[0])
    motes = sorted((int(mote) for mote in sys.stdin.readline().split()),
                   reverse=True)
    min_changes = sys.maxsize
    num_changes = 0
    while motes and num_changes <= min_changes:
        min_changes = min(min_changes, num_changes + len(motes))
        mote = motes.pop()
        while armins_mote <= mote:
            armins_mote += armins_mote - 1
            num_changes += 1
            if num_changes >= min_changes:
                break
        else:
            armins_mote += mote
    print('Case #{}: {}'.format(case, min(min_changes, num_changes)))
