import sys

f = [sys.stdin]


def replace_stdin():
    print("WARNING! replacing stdin")
    # print("WARNING! replacing stdin", file=sys.stderr)
    f[0] = open('in', 'r')

# replace_stdin()


def solve(setup, k):
    setup = list(setup)
    flips = 0

    def flip(l, pos, length):
        for d in range(length):
            j = d + pos
            l[j] = '+' if l[j] == '-' else '-'

    for i in range(0, (len(setup) - k) + 1):
        if setup[i] == '-':
            flips += 1
            flip(setup, i, k)

    if setup != list('+' * len(setup)):
        return None
    return flips


def ln():
    return f[0].readline()


def solve_codejam():
    tests = int(ln())
    for test_nr in range(1, tests + 1):
        setup, k = ln().strip().split()
        k = int(k)
        result = solve(setup, k)
        if result == None:
            result = "IMPOSSIBLE"
        print("Case #%d: %s" % (test_nr, str(result)))

solve_codejam()