#!/usr/bin/python
import sys
import string

# n=3
# scale=8
# cutoff=4
# 0 0 0 0
# 1 0 0 1
# 0 1 0 2
# 1 1 0 3
# 0 0 1 4
# 1 0 1 5
# 0 1 1 6
# 1 1 1 7


def find_state(n, k):
    scale = pow(2, n)
    cutoff = scale / 2
    if (k % scale) == scale - 1:
        return "ON"
    else:
        return "OFF"

tests = int(sys.stdin.readline())
for test in range(tests):
    line = sys.stdin.readline()
    words = string.split(line)
    n = int(words[0])
    k = int(words[1])
    state = find_state(n, k)
    print "Case #%d: %s" % (test+1, state)

