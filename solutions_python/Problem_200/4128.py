import sys
from typing import List

#T: number of test cases
#N: the last number tatiana counted

def int_to_digit_list(n: int) -> List[int]:
    return [int(d) for d in str(n)]

def is_tidy(n: int):
    digit_list = int_to_digit_list(n)
    return is_tidy_digit_list(digit_list)

def is_tidy_digit_list(digit_list: List[int]):
    previous_digit = 0

    for d in digit_list:
        if d < previous_digit:
            return False
        previous_digit = d
    return True

def digit_list_to_int(digit_list: List[int]) -> int:
    return int(''.join([str(d) for d in digit_list]), base=10)

def ninify(digit_list: List[int], ninification_index: int):
    if ninification_index == 0:
        raise Exception('ninification index == 0')
    if digit_list[ninification_index] == 9:
        raise Exception('index already ninified')

    for i in range(ninification_index, 0, -1):
        digit_list[i] = 9
        if digit_list[i-1] > 0:
            digit_list[i-1] -= 1
            return

    raise Exception('unable to ninify')

def get_ninification_index(digit_list: List[int]) -> int:
    for i in range(len(digit_list) - 1, 0, -1):
        if digit_list[i] != 9:
            return i
    raise Exception('ninification index not found!')

def last_tidy_number(N: int) -> int:
    digit_list = int_to_digit_list(N)

    while not is_tidy_digit_list(digit_list):
        ninify(digit_list, get_ninification_index(digit_list))

    return digit_list_to_int(digit_list)

def answer(N: int) -> int:
    return last_tidy_number(N)

def main():
    inputfile = sys.stdin
    T = int(inputfile.readline()) #number of test cases

    for test_case_num in range(1, T + 1):
        N = int(inputfile.readline().strip())
        print('Case #{test_case_num}: {test_case_answer}'.format(
            test_case_num=test_case_num,
            test_case_answer=answer(N)))

if __name__ == '__main__':
    main()