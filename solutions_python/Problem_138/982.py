def solve_regular(case):
    naomi = sorted(case[0])
    ken = sorted(case[1])
    N = len(naomi)

    score = 0
    for i in reversed(range(N)):
        naomi_choice = naomi[i]
        if naomi[i] > ken[i]:
            score += 1
            ken.pop(0)
        else:
            ken.pop(i)
    return score


def solve_deceitful(case):
    naomi = sorted(case[0])
    ken = sorted(case[1])
    N = len(naomi)

    score = 0
    for i in range(N):
        if naomi[0] > ken[0]:
            score += 1
            ken.pop(0)
            naomi.pop(0)
        else:
            ken.pop(-1)
            naomi.pop(0)
    return score


def parse_cases(f):
    """
    Yields a series of ([naomi_weights], [ken_weights])
    suitable for passing to solve_case.
    """

    cases = int(f.readline())
    for i in xrange(cases):
        N = int(f.readline())
        naomi_weights = map(float, f.readline().split())
        ken_weights = map(float, f.readline().split())
        yield (naomi_weights, ken_weights)


if __name__ == "__main__":
    import sys
    for i, case in enumerate(parse_cases(sys.stdin)):
        deceitful_score = solve_deceitful(case)
        regular_score = solve_regular(case)
        print "Case #{}: {} {}".format(i+1, deceitful_score, regular_score)