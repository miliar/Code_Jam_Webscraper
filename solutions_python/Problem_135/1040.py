SIZE = 4
ENTRIES = 2

def solve_case(case):
    options = set(range(1, SIZE*SIZE + 1))
    for arrangement, answer in case:
        options &= set(arrangement[answer-1])
    return options


def parse_cases(f):
    """
    Yields a series of [(arrangement, answer), (arrangement, answer)]
    suitable for passing to solve_case.
    """

    cases = int(f.readline())
    for i in xrange(cases):
        case = []
        for j in xrange(ENTRIES):
            answer = int(f.readline())
            arrangement = []
            for k in xrange(SIZE):
                arrangement.append(map(int, f.readline().split()))
            case.append((arrangement, answer))
        yield case


if __name__ == "__main__":
    import sys
    for i, case in enumerate(parse_cases(sys.stdin)):
        options = solve_case(case)
        if len(options) == 1:
            result = next(iter(options))
        elif not options:
            result = "Volunteer cheated!"
        else:
            result = "Bad magician!"
        print "Case #{}: {}".format(i+1, result)