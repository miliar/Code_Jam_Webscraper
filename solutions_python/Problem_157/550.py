import sys


INDEXES = ['', '1', 'i', 'j', 'k']
MULT = [
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 4],
    [0, 2, -1, 4, -3],
    [0, 3, -4, -1, 2],
    [0, 4, 3, -2, -1],
]
REVR = {
    'i': {-4: -3, -3: 4, -2: -1, -1: 2, 1: -2, 2: 1, 3: -4, 4: 3},
    'j': {-4: 2, -3: -1, -2: -4, -1: 3, 1: -3, 2: 4, 3: 1, 4: -2},
    'k': {-4: -1, -3: -2, -2: 3, -1: 4, 1: -4, 2: -3, 3: 2, 4: 1},
}


def rough_sign(x):
    return -1 if x < 0 else 1


def next_numstra(stra):
    if len(stra) < 2:
        return None
    first = stra.pop(0)
    second = stra[0]
    stra[0] = rough_sign(first) * rough_sign(second) * MULT[abs(first)][abs(second)]
    return stra


def mul_all(stra):
    muled = 1
    for s in stra:
        muled = rough_sign(muled) * rough_sign(s) * MULT[abs(muled)][abs(s)]
    return muled


def r_check(r):
    if len(r) < 1:
        return False

    x = r[0]
    for n in r[1:]:
        if x == 3:
            return True

        x = rough_sign(x) * rough_sign(n) * MULT[abs(x)][abs(n)]
    return False


def solve_case(dijkstra, times, case_number):
    numstra = [INDEXES.index(s) for s in dijkstra * times]

    if len(numstra) < 3:
        print "Case #%d: NO" % case_number
        return

    if len(set(numstra)) < 2:
        print "Case #%d: NO" % case_number
        return

    if mul_all(numstra) != -1:
        print "Case #%d: NO" % case_number
        return

    l = numstra[0]
    r = mul_all(numstra[1:])
    for idx, m in enumerate(numstra[1:]):
        if l == 2:
            if r_check(numstra[idx + 1:]):
                print "Case #%d: YES" % case_number
                return

        l = rough_sign(l) * rough_sign(m) * MULT[abs(l)][abs(m)]
        r = REVR[INDEXES[m]][r]

    print "Case #%d: NO" % case_number


def main():
    r = sys.stdin

    if len(sys.argv) > 1:
        r = open(sys.argv[1], 'r')

    total_cases = r.readline()
    for case_number in range(1, int(total_cases) + 1):
        times = int(r.readline().strip().split(' ')[1])
        solve_case(r.readline().strip(), times, case_number)


if __name__ == '__main__':
    main()
