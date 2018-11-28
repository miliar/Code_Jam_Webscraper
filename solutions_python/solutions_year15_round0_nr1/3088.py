#!/usr/bin/env

import sys

def min_number_of_friends(current_state):
    extra_friends = 0
    # i -> shyness level
    # current_state[i] -> how many people have shynees level i
    for i in xrange(1, len(current_state)):
        clapping = current_state[i-1]
        seating = current_state[i]
        if clapping >= i:
            current_state[i] += clapping
        else:
            extra = i - clapping
            current_state[i] += clapping + extra
            extra_friends += extra
    return extra_friends


if __name__ == '__main__':
    f = sys.stdin
    test_cases = int(f.readline())
    for i in xrange(test_cases):
        shiest, nk = f.readline().replace('\n', '').split(' ')
        shiest = int(shiest)
        nk = list(nk)
        nk = map(int, nk)
        mfriends = min_number_of_friends(nk)
        print("Case #%d: %d" % (i+1, mfriends))

