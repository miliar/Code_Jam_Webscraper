#!/usr/bin/env python2.7

# Standard libs
import math
import sys

# Constants
USAGE = "python %s INPUT_FILE" % (sys.argv[0])
PRECOMPUTED_UPPER_BOUND = 10**14

def main(argv):
    if len(argv) != 2:
        raise Exception("Invalid arguments! Usage: %s" % (USAGE))

    input_filename = argv[1]

    # Pre-compute all fair-and-square numbers up to an absolute upper bound
    precomputed_fair_and_squares = get_fair_and_square_numbers(
                                       PRECOMPUTED_UPPER_BOUND)

    with open(input_filename, "r") as input_file:
        # Read in the number of test cases
        try:
            num_test_cases = int(input_file.readline().strip())
        except:
            raise Exception("Invalid input file")

        # Count the number of fair-and-square numbers for each test case
        for test_case_number in range(1, num_test_cases + 1):
            lower, upper = map(int, input_file.readline().strip().split())
            fair_and_square_count = count_fair_and_square_numbers(lower,
                                        upper, precomputed_fair_and_squares)
            print "Case #%d: %s" % (test_case_number, fair_and_square_count)

def count_fair_and_square_numbers(inclusive_lower_bound,
                                  inclusive_upper_bound,
                                  precomputed_fair_and_squares):
    def bounds(x):
        return x >= inclusive_lower_bound and x <= inclusive_upper_bound

    return len(filter(bounds, precomputed_fair_and_squares))

# Retrieve the set of fair-and-square numbers up to the upper bound
def get_fair_and_square_numbers(inclusive_upper_bound):
    fair_and_square_numbers = []

    for fair_and_square in fair_and_squares(1):
        if fair_and_square > inclusive_upper_bound:
            break
        fair_and_square_numbers.append(fair_and_square)

    return fair_and_square_numbers

# Generator for fair and square numbers
def fair_and_squares(start=1):
    i = int(math.ceil(math.sqrt(start)))

    while True:
        i_squared = i**2
        if is_palindrome(i) and is_palindrome(i_squared):
            yield i_squared
        i += 1

def is_palindrome(i):
    s = str(i)
    return s == ''.join(reversed(s))

if __name__ == "__main__":
    main(sys.argv)
