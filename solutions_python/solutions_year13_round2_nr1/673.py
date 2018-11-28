#!/usr/bin/env python


def compute_add(blob, target):
    count = 0
    while blob <= target:
        # print "Adding: " + str(blob)
        blob += blob - 1
        count += 1
    return (count, blob)

import sys
sys.stdin = open("a_in", "r")
sys.stdout = open("a_out", "w")
test_cases = int(raw_input())
for test_case in xrange(test_cases):
    line1 = raw_input().split()
    blob = int(line1[0])
    line2 = raw_input().split()
    motes = [0] + sorted([int(x) for x in line2])

    actions = 0
    blob_size = [blob]
    i = 1
    while i < len(motes):
        # check if blob can devour this mote
        # print blob_size
        # print motes
        # print actions
        if blob_size[i - 1] > motes[i]:
            # all good, carry on
            blob_size.append(blob_size[i - 1] + motes[i])
            i += 1
        else:
            amount_to_subtract = len(motes) - i
            if blob_size[i - 1] > 1:
            # compute the amount we need to add or subtract
                amount_to_add, new_blob = compute_add(blob_size[i - 1], motes[i])
                if amount_to_add < amount_to_subtract:
                    actions += amount_to_add
                    blob_size[i - 1] = new_blob
                else:
                    actions += amount_to_subtract
                    break
            else:
                actions += amount_to_subtract
                break

    print "Case #%i: %i" % (test_case + 1, actions)
