#!/usr/bin/env python3


def first_bad_digit(n_list):
    for idx, (a, b) in enumerate(zip(n_list, n_list[1:])):
        if a > b:
            return idx + 1

    return -1


num_cases = int(input())

for case in range(1, num_cases+1):
    n_list = list(input())

    fbd = first_bad_digit(n_list)
    while fbd != -1:
        n_list[fbd:] = ['0' for _unused in n_list[fbd:]]
        n_list = list(str(int(''.join(n_list)) - 1))
        fbd = first_bad_digit(n_list)

    answer = ''.join(n_list)

    print("Case #{case}: {answer}".format(case=case, answer=answer))
