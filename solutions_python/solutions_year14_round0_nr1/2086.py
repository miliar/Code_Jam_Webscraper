#! /usr/bin/env python

read_int = lambda: int(raw_input())

def read_arrangement():
    return [list(map(int, raw_input().split())) for __ in range(4)]

def analyze(r1, a1, r2, a2):
    s = set(a1[r1-1]) & set(a2[r2-1])
    if len(s) > 1:
        return "Bad magician!"
    elif len(s) == 0:
        return "Volunteer cheated!"
    else:
        return s.pop()

T = read_int()
for case in range(T):
    response1 = read_int()
    arrangement1 = read_arrangement()
    response2 = read_int()
    arrangement2 = read_arrangement()
    print "Case #{}: {}".format(case + 1,
            analyze(response1, arrangement1, response2, arrangement2))
