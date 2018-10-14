#! /usr/bin/env python
import sys
import math

def read_input():
    with open(sys.argv[1]) as input_file:
        num_cases = int(input_file.readline())
        cases = [[int(token) for token in line.split()] for line in input_file]
    return num_cases, cases

def is_palindrome(some_number):
    num_string = str(some_number)
    return num_string == num_string[::-1]

def main():
    num_cases, cases = read_input()
    fs_numbers = set()
    non_fs_numbers = set()
    counts = [0 for _ in xrange(num_cases)]
    for i, case in enumerate(cases):
        for test in xrange(case[0], case[1] + 1):
            if test in fs_numbers:
                counts[i] += 1
            elif test not in non_fs_numbers:
                if is_palindrome(test):
                    root = math.sqrt(test)
                    root_int = int(root)
                    if root == root_int:
                        if is_palindrome(root_int):
                            counts[i] += 1
                            fs_numbers.add(test)
                        else:
                            non_fs_numbers.add(test)
                    else:
                        non_fs_numbers.add(test)
                else:
                    non_fs_numbers.add(test)
    print fs_numbers

    with open(sys.argv[2], 'w') as out_file:
        for i, count in enumerate(counts, start=1):
            out_string = 'Case #{}: '.format(i)
            out_string += str(count)
            out_file.write(out_string + '\n')

if __name__ == '__main__':
    # run as $ python fair_square.py input.txt output.txt
    main()
