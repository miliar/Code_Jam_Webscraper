from __future__ import absolute_import, division, print_function
import sys


def solve(horses, distances, start, dest, time=0, d=0, s=0):

    to_travel = distances[start]

    if d < to_travel:
        return sys.maxint

    d -= to_travel
    time += to_travel / float(s)

    if start + 1 == dest:
        return time

    alt_d, alt_s = horses[start+1]
    a = solve(horses, distances, start+1, dest, time, alt_d, alt_s)
    b = solve(horses, distances, start+1, dest, time, d, s)
    return min(a, b)

def solvebac


#with open('sample.in') as f:
with open('C-small-attempt0.in') as f:
#with open('A-large.in') as f:
    T = int(f.readline())

    for puzzle_count in range(T):
        n, q = map(int, f.readline().strip().split(' ')) # cities, stop_pairs

        horses = {}
        for i in range(0, n):
            raw = f.readline().strip().split(' ')
            e, s = map(int, raw) # distance, speed
            horses[i+1] = (e, s)

        # flatern
        distances = {}
        for i in range(0, n):
            raw = f.readline().strip().split(' ')
            dist = [a for a in map(int, raw) if a != -1]
            if dist:
                distances[i+1] = dist[0]
            else:
                distances[i+1] = -1

        for i in range(0, q):
            raw = f.readline().strip().split(' ')
            start, dest = map(int, raw)

        d, s = horses[start]
        ans = solve(horses, distances, start, dest, 0, d, s)

        print('Case #%s: %f' % (str(puzzle_count + 1), ans))

