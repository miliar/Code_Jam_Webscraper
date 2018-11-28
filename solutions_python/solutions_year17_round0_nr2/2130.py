def parse_input():
    data = []
    with open('B-small-attempt1.in', 'r') as f:
        for line in f:
            data.append(line.strip('\n'))
    T = int(data[0])
    cases = []
    for i in range(T):
        cases.append(int(data[1 + i]))
    return T, cases


def solve_case(case):
    while True:
        lcase = list(str(case))
        maxindex = len(lcase) - lcase[::-1].index(max(lcase)) - 1
        if len(lcase) - 1 > maxindex:
            lcase = lcase[:maxindex] + [str(int(lcase[maxindex]) - 1)] + list(len(lcase[maxindex + 1:])*'9')
            case = int("".join(lcase))
        if sorted(lcase) == lcase:
            return case
        case -= 1


T, cases = parse_input()
for c, case in enumerate(cases):
    attempts = solve_case(case)
    print('Case #{}: {}'.format(c + 1, attempts))
