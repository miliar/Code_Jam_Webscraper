from __future__ import absolute_import, division, print_function


def time(k, s, d):
    distance = d - k
    return distance / float(s)

def solve(slowest, d):
    return d/slowest

#with open('sample.in') as f:
#with open('A-small-attempt0.in') as f:
with open('A-large.in') as f:
    T = int(f.readline())

    for puzzle_count in range(T):
        d, h = map(int, f.readline().strip().split(' '))
        slowest = 0

        for i in range(0, h):
            raw = f.readline().strip().split(' ')
            k, s = map(int, raw)
            time_taken = time(k, s, d)
            if time_taken > slowest:
                slowest = time_taken

        ans = solve(slowest, d)

        print('Case #%s: %f' % (str(puzzle_count + 1), ans))

