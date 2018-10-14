"""
Solve Fair and Square problem.
"""

#
# Notes: - Python 2.7 required (for argparse)
#

import argparse
from itertools import chain
from bisect import bisect_left, bisect_right

def main():
    args = parse_argumnets()
    solve(args.input, args.output)

def parse_argumnets():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', default='input.txt')
    parser.add_argument('--output', default='output.txt')
    return parser.parse_args()

def solve(input_file_name, output_file_name):
    input = open(input_file_name, 'r').read()
    cases = parse_input(input)

    merged_cases = merge_ranges(cases)

    fair_and_square_numbers = chain(*(get_fair_and_square_numbers(case) for case in merged_cases))
    # Note: The numbers should be generated in order, but just in case...
    fair_and_square_numbers = sorted(fair_and_square_numbers)

    solutions = []
    for lower_bound, upper_bound in cases:
        start_index = bisect_left(fair_and_square_numbers, lower_bound)
        end_index = bisect_right(fair_and_square_numbers, upper_bound)
        solution = len(fair_and_square_numbers[start_index:end_index])
        solutions.append(solution)

    formatted_solution = format_solutions(solutions)

    open(output_file_name, 'w').write(formatted_solution)

# Adapted from http://stackoverflow.com/a/5679899
def merge_ranges(ranges):
    sorted_ranges = sorted(ranges)
    saved = list(sorted_ranges[0])
    for st, en in sorted_ranges:
        if st <= saved[1]:
            saved[1] = max(saved[1], en)
        else:
            yield tuple(saved)
            saved[0] = st
            saved[1] = en
    yield tuple(saved)


def parse_input(input):
    lines = [l.strip() for l in  input.splitlines() if l.strip() != '']
    current_line = 0

    cases_count = int(lines[current_line])
    current_line += 1

    cases = []
    for i in xrange(cases_count):
        bounds = parse_ints(lines[current_line])
        current_line += 1

        assert len(bounds) == 2

        cases.append(bounds)

    return cases

def parse_ints(string):
    return [int(s) for s in string.split()]

def get_fair_and_square_numbers(bounds):
    return list(generate_fair_and_square_numbers(bounds))

def generate_fair_and_square_numbers(bounds):
    lower_bound, upper_bound = bounds

    root_lower_bound = isqrt(lower_bound)
    # round up if needed
    if root_lower_bound ** 2 != lower_bound:
        root_lower_bound += 1

    root_upper_bound = isqrt(upper_bound)

    for root in generate_numbers(root_lower_bound, root_upper_bound):
        if is_palindrome(root):
            square = root * root
            if is_palindrome(square):
                yield square


## {{{ http://code.activestate.com/recipes/577821/ (r1)
def isqrt(x):
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y
## end of http://code.activestate.com/recipes/577821/ }}}

def generate_numbers(lower_bound, upper_bound):
    # Note: xrange is not good because it doesn't support large numbers.
    x = lower_bound
    while x <= upper_bound:
        yield x
        x += 1

def is_palindrome(number):
    number_string = str(number)
    return number_string == ''.join(reversed(number_string))

def format_solutions(solutions):
    format = 'Case #%d: %d'
    return '\n'.join(format % (i + 1, s) for i, s in enumerate(solutions))

if __name__ == '__main__':
    main()
