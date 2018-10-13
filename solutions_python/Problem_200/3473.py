#!/usr/bin/env python3


def is_tidy(number):
    str_number = str(number)
    return all(x > y for x, y in zip(str_number, str_number[1:]))


def is_tidy(number):
    n = str(number)
    return sorted(n) == list(n)


def biggest_tidy_number(up_to):
    for i in range(up_to, 1, -1):
        str_number = str(i)
        if all([x > y for x, y in zip(str_number, str_number[1:])]):
            return i
    return 0


def biggest_tidy_number(up_to):
    for i in range(up_to, 0, -1):
        if is_tidy(i):
            return i
    return 0


def biggest_tidy_number_less_than(number):
    digits = list(str(number))
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] < digits[i - 1]:
            # Have to fix
            for di in range(i, len(digits)):
                digits[di] = '9'
            digits[i - 1] = str(int(digits[i - 1]) - 1)
    return int(''.join(digits))


if __name__ == '__main__':
    import sys
    test_cases = None
    case = 1
    with open(sys.argv[1]) as infile:
        for line in infile:
            line = line.strip()
            if test_cases is None:
                test_cases = line
                continue
            print("Case #{}: {}".format(
                case, biggest_tidy_number_less_than(int(line))))
            case += 1
