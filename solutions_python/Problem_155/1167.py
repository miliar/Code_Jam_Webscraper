__author__ = 'moritz'


def solver(s):
    return max([max(0, 1 + i - e) for i, e in enumerate(cumsum(s[:-1]))] + [0])


def cumsum(it):
    total = 0
    for x in it:
        total += x
        yield total


def solve_case(test_case):
    case = raw_input().split()
    smax = int(case[0])
    s_string = case[1]
    s = [int(s_char) for s_char in s_string]
    soln = solver(s)
    print("Case #{}: {}".format(test_case + 1, soln))


t = input()

for test_case in range(t):
    solve_case(test_case)