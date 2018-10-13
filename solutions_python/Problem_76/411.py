#! /usr/bin/python
# GCJ 2011 QR - Candy Splitting

from sys import stdin


def parse_test_case(raw_test_case) :
    return [ int(x) for x in raw_test_case[1].strip().split(' ') ]


def divide_candy(candy_list) :
    patricks_sum = 0
    for c in candy_list :
        patricks_sum ^= c

    if patricks_sum == 0 :
        return str(sum(candy_list) - min(candy_list))
    else :
        return 'NO'


def print_solution(case_id, solution) :
    print('Case #{0}: {1}'.format(case_id, solution))


def main() :
    input_data = stdin.readlines()

    n_tests = int(input_data[0])
    for i in range(1, n_tests + 1) :
        candy_list = parse_test_case(input_data[i*2-1:i*2+1])
        solution = divide_candy(candy_list)
        print_solution(i, solution)

if __name__ == '__main__' :
    main()
