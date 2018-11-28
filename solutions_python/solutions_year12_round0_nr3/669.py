# recycled numbers - brute force appriach
#
import sys


def main():
    tests = read_input()
    #import pprint; pprint.PrettyPrinter(indent=4, width=10).pprint(tests); return
    results = map(solve, tests)
    print_results(results)


def read_input():
    # read input from stdin
    lines = map(lambda line: line.strip('\n'), sys.stdin.readlines())

    # parse it out
    num_tests = int(lines[0])
    lines = lines[1:]

    tests = []
    for i in range(num_tests):
        tests.append(map(int, lines[i].split()))

    return tests


def print_results(results):
    for i, r in enumerate(results):
        print 'Case #%d: %s' % (i + 1, r)


def solve(test):
    A, B = test
    pairs = []
    for i in xrange(A, B+1):
        if i < 10:
            continue
        s = str(i)
        for r in xrange(1, len(s)):
            t = s[r:] + s[0:r]
            if t[0] == '0':
                continue
            if t == s:
                continue
            if int(t) < A or int(t) > B:
                continue
            #print i, r, t
            pairs.append((s, t))
    return len(set(pairs)) / 2

main()
