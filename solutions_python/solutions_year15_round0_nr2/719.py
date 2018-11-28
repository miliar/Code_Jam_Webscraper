#!/usr/bin/python
import fileinput


def get_cases():
    inp = fileinput.input()
    num_cases = int(inp.next())
    for _ in xrange(num_cases):
        inp.next()
        line = inp.next().strip()
        yield list(reversed(sorted(map(int, line.split()))))


def could_redistribute(case):
    if case[0] <= 3:
        return False
    else:
        return True


def redistribute3(case):
    remainder = case[0]/3
    case.append(remainder)
    case.append(remainder)
    case[0] = case[0] - remainder - remainder
    return list(reversed(sorted(case)))


def redistribute(case):
    remainder = case[0]/2
    case.append(remainder)
    case[0] = case[0] - remainder
    return list(reversed(sorted(case)))


def work(case):
    for num in case:
        num -= 1
        if num > 0:
            yield num


def solve(case, cost=1):
    if len(case) == 0:
        return 0, [], 0
    while len(case) > 0:
        copy = list(case)
        if could_redistribute(case):
            case_1 = solve(redistribute(list(case)))
            if case[0] > 6:
                case_2 = solve(redistribute3(list(case)), cost=2)
            else:
                case_2 = (1000000, None, None)
            case_3 = solve(list(work(case)))
            x = min(case_1[0], case_2[0], case_3[0])
            for i in [case_3, case_2, case_1]:
                if i[0] == x:
                    i[1].append(copy)
                    return (i[0] + cost, i[1], i[2])
        else:
            x, y, z = solve(list(work(case)))
            y.append(copy)
            return (x + cost, y, z)


if __name__ == '__main__':
    for num, case in enumerate(get_cases(), 1):
        solution, chain, splitted = solve(case)
        print('Case #%d: %d' % (num, solution))
