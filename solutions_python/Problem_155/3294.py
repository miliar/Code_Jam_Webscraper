#! /usr/env/bin python

from __future__ import print_function, absolute_import


def get_friends(case):
    friend_count = 0
    standing_count = 0
    for shy_idx, shy_folks in enumerate(case):
        shy_folks = int(shy_folks)
        audience_needed = shy_idx
        if audience_needed > (standing_count + friend_count):
            friend_count += audience_needed - (standing_count + friend_count)
        standing_count += shy_folks
    return friend_count

if __name__ == '__main__':
    case_count = int(raw_input())
    test_cases = []
    for test_case in range(case_count):
        max_shyness, audience_shyness = raw_input().split(' ')
        test_cases.append(audience_shyness)

    for idx, case in enumerate(test_cases):
        friends = get_friends(case)
        print('Case #{idx}: {friends}'.format(idx=idx+1, friends=friends))
