import sys

from collections import defaultdict

f = [sys.stdin]


def replace_stdin():
    print("WARNING! replacing stdin")
    print("WARNING! replacing stdin", file=sys.stderr)
    f[0] = open('in', 'r')

# replace_stdin()

def ln():
    return f[0].readline()

def reduce(first_size, steps):
    state = defaultdict(int)
    state[first_size] = 1

    while True:
        max_sz = max(state.keys())
        minDst = (max_sz-1) // 2
        maxDst = max_sz // 2
        red_size = min(steps, state[max_sz])
        state[minDst] += red_size
        state[maxDst] += red_size
        state[max_sz] -= red_size
        if state[max_sz] == 0:
            del state[max_sz]
        steps -= red_size
        if steps == 0:
            return minDst, maxDst


def solve_codejam():
    tests = int(ln())
    for test_nr in range(1, tests + 1):
        n, k = map(int, ln().strip().split())
        mind, maxd = reduce(n, k)
        print("Case #%d: %d %d" % (test_nr, maxd, mind))

solve_codejam()
