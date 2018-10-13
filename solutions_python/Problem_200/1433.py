def to_list(number):
    return [int(c) for c in str(number)]


n = int(input())
cases = []
for _ in range(n):
    cases.append([int(c) for c in input()])


def to_string(case):
    return "".join(str(i) for i in case)


def to_int(case):
    return int(to_string(case))


def is_tidy(case):
    for i in range(1, len(case)):
        if case[i-1] > case[i]:
            return False
    return True


def do(case):
    """
    Man's an algorithm.
    """
    c = 1
    while not is_tidy(case):
        case = to_int(case)
        case = (case - case % (10**c)) - 1
        case = to_list(case)
        c += 1
    return case


for index, case in enumerate(cases):
    print("Case #{}: {}".format(index+1, to_string(do(case))))
