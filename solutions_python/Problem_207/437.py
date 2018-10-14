#!/usr/bin/env python2.7
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def isPossible(N, l):
    for color in l:
        if color > N/2:
            return False
    return True

def solve(N, R, O, Y, G, B, V):
    if not isPossible(N, [R, O, Y, G, B, V]):
        return 'IMPOSSIBLE'

    color_dict = {
        'R': R,
        'O': O,
        'Y': Y,
        'G': G,
        'B': B,
        'V': V

    }
    max_v = -1
    for k, v in color_dict.iteritems():
        if v > max_v:
            max_v = v
            max_k = k
    color_dict[max_k] -= 1

    head = max_k
    result = max_k
    prev = max_k
    for _ in xrange(N-1):
        max_v = -1
        for k, v in color_dict.iteritems():
            if (v > max_v or (v == max_v and k == head)) and k != prev:
                max_v = v
                max_k = k
        if max_v <= 0:
            return 'IMPOSSIBLE'
        result += max_k
        prev = max_k
        color_dict[max_k] -= 1
    return result

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    N, R, O, Y, G, B, V = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case

    print "Case #{}: {}".format(i, solve(N, R, O, Y, G, B, V))
    # check out .format's specification for more formatting options
