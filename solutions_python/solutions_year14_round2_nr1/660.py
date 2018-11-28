#!/usr/bin/env python
# vim: set filetype=python et sw=4 ts=4:

import sys
import collections

T = int(sys.stdin.readline())

def get_string_count(s):
    counts = [1]
    chars = [s[0]]
    count_idx = 0
    for c in s[1:]:
        if c == chars[count_idx]:
            counts[count_idx] += 1
        else:
            chars.append(c)
            counts.append(1)
            count_idx += 1
    return chars, counts

def solve(strings):
    answer = 0
    chars, counts = get_string_count(strings[0])
    C = [counts]
    for _ in strings[1:]:
        new_chars, counts = get_string_count(_)
        if chars != new_chars:
            return None
        else:
            C.append(counts)

    N = len(C)
    columns = [[C[row][column] for row in xrange(N)] for column in xrange(len(C[0]))]
    for i in columns:
        colsum = sum(i)
        target_value = int(round(colsum/float(len(i))))
        answer += sum((abs(target_value - x) for x in i))

    return answer

for case in xrange(T):
    N = int(sys.stdin.readline())
    strings = []
    for _ in xrange(N):
        strings.append(sys.stdin.readline().strip())

    sys.stdout.write("Case #%d: " % (case + 1))
    result = solve(strings)
    if result == None:
        sys.stdout.write("Fegla Won\n")
    else:
        sys.stdout.write("%d\n" % (result))

