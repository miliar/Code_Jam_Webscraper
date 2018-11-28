#!/usr/bin/env python

# INPUT_FILE = 'sample.in'
INPUT_FILE = 'A-small-attempt0.in'
fp = open(INPUT_FILE, 'r')

NUM_TESTS = int(fp.readline())
TESTS = []
for i in range(NUM_TESTS):
    N = int(fp.readline())
    strings = []
    for j in range(N):
        strings.append(fp.readline().strip())
    TESTS.append(tuple(strings))
TESTS = tuple(TESTS)
fp.close()
# print TESTS


def parse_string(s):
    res = []
    prev = None
    sub_string = None
    for i in s:
        if prev != i:
            res.append(sub_string)
            prev = i
            sub_string = i
        else:
            sub_string += i
    res.append(sub_string)
    return tuple(res[1:])

# print parse_string('mmaw')
# print parse_string('mawmmm')


def solve(strings):
    N = len(strings)

    parsed = []
    s0 = strings[0]
    p0 = parse_string(s0)
    parsed.append(p0)
    L = len(p0)
    # print parsed
    # print L

    for s in strings[1:]:
        p = parse_string(s)
        # print p
        if len(p) != L:
            return None
        for j in range(L):
            if p[j][0] != p0[j][0]:
                return None
        parsed.append(p)
    parsed = tuple(parsed)
    # print parsed

    min_moves = 0
    for i in range(L):
        total = 0
        for j in range(N):
            p = parsed[j][i]
            # print p,
            total += len(p)
            # print total
        average = total // N
        # print average
        for j in range(N):
            p = parsed[j][i]
            min_moves += abs(len(p) - average)
            # print p, min_moves
    return min_moves


def main():
    for i in range(NUM_TESTS):
        res = solve(TESTS[i])
        print 'Case #%d:' % (i + 1),
        if res is None:
            print 'Fegla Won'
        else:
            print res


if __name__ == '__main__':
    main()
