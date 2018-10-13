import math

def write_solutions(solutions):
    f = open('prob_A_large.output', 'w')
    for i, sol in enumerate(solutions):
        f.write('Case #%d: %.9f\n' % ((i + 1), sol))
    f.close()



def solve_cases(cases):
    for j, case in enumerate(cases):
        print 'solving %d' % (j + 1)
        yield solve_A(case[0][0], case[0][1], case[1])



def solve_A(N, K, pancakes):
    max_coverage = None
    for i, pancake in enumerate(pancakes):
        coverage = solve_A_given_bottom(N, K, pancakes, i)
        if max_coverage is None:
            max_coverage = coverage
            continue
        max_coverage = max(coverage, max_coverage)
    return max_coverage


def solve_A_given_bottom(N, K, pancakes, bottom_ind):
    bottom = pancakes[bottom_ind]
    bottom_R, bottom_H = bottom
    candidates = []
    for i, p in enumerate(pancakes):
        if i == bottom_ind:
            continue
        if p[0] > bottom_R:
            continue
        candidates.append(p)
    candidates.sort(key=lambda x: -(x[0] * x[1]))
    choices = candidates[:K-1]
    if len(choices) < K - 1:
        return 0
    coverage = (bottom_R ** 2)
    coverage += sum([2 * p[0] * p[1] for p in (choices + [bottom])])
    coverage *= math.pi
    return coverage


def parse_input(stream):
    num_cases = None
    test_cases = []
    in_test_case = False
    cur_N = None
    cur_K = None
    pancakes_left_in_case = None
    cur_test_case = []
    for i, line in enumerate(stream):
        if i == 0:
            num_cases = int(line.strip())
            in_test_case = False
            continue
        if not in_test_case:
            cur_N, cur_K = line.strip().split(' ')
            cur_N = int(cur_N)
            cur_K = int(cur_K)
            in_test_case = True
            pancakes_left_in_case = cur_N
            cur_test_case.append((cur_N, cur_K))
            cur_test_case.append([])
            continue
        R, H = line.strip().split(' ')
        R = int(R)
        H = int(H)
        cur_test_case[-1].append((R, H))
        pancakes_left_in_case -= 1
        if pancakes_left_in_case == 0:
            test_cases.append(cur_test_case)
            cur_test_case = []
            in_test_case = False
    return test_cases


if __name__ == '__main__':
    f = open('/Users/jakemagner/Desktop/google_code_jam/r1/A-large.in')
    # f = open('/Users/jakemagner/Desktop/google_code_jam/r1/probA_example.inp')
    cases = parse_input(f)
    write_solutions(solve_cases(cases))
