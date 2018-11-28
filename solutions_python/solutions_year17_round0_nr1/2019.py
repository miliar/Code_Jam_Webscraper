"none"
import fileinput
import math
import heapq
from collections import deque
import time


def test():
    "none"
    assert flip("--+") == "++-"
    assert solve_simple("---+-++-", 3) == 3
    assert solve_simple("-+-+-", 4) is None
    assert solve_simple("+--", 2) == 1
    assert solve_simple("+++", 3) == 0
    assert solve_simple("---", 3) == 1

def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

def solve_simple(line, size):
    "none"
    """
    2
    +--


    +---

    -++-
    +---
    ---+

    +--+
    """
    seen = set([])
    q = deque([(0, line)])
    needed = '+' * len(line)
    while len(q) > 0:
        num, line = q.popleft()
        if line == needed:
            return num
        for i, ngram in enumerate(find_ngrams(line, size)):
            start = i
            end = start+size
            new_line = line[:start] + flip(ngram) + line[end:]
            if new_line in seen:
                continue
            seen.add(new_line)
            q.append((num+1, new_line))
    return None

def flip(ngram):
    return ''.join(map(lambda c: '-' if c == '+' else '+', ngram))


test()

for i, line in enumerate(fileinput.input()):
    if i == 0:
        continue
    N, size = line.strip().split(" ")
    res = solve_simple(N, int(size))
    if res is None:
        res = "IMPOSSIBLE"
    print "Case #%d: %s" % (i, res)
    # print N, size, solve(int(N), int(size)), solve_simple(int(N), int(size))

# for i in xrange(1, 100):
#     for j in xrange(1, 10**9):
#         pass
#     print i, j

"""
# 0 . . 0
"""