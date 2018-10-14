import sys
from math import sqrt


# Stores previously determined results with key of n and value of True/False.
result_cache = {}


def is_perfect_square(n):
    """Returns whether or not the specified int is a perfect square."""
    return int(sqrt(n) + 0.5) ** 2 == n


def is_fair_and_square(n):
    """
    Returns whether the specified int is "fair and square":
    both a palindrome and the square of a palindrome
    """
    num_str = str(n)
    if num_str == num_str[::-1]:
        if is_perfect_square(n):
            sqrt_str = str(int(sqrt(n)))
            return sqrt_str == sqrt_str[::-1]
    return False


def run_test_case(case_num, a, b):
    """
    Runs a test case with specified case_num from a to b inclusive.
    """
    num = 0
    for n in xrange(a, b + 1):
        if result_cache.get(n):
            num += 1
            continue
        result = is_fair_and_square(n)
        if result:
            num += 1
        result_cache[n] = result
    print 'Case #%i: %i' % (case_num, num)


if __name__ == '__main__':
    num_cases = None
    case_num = 1
    for line in sys.stdin:
        if num_cases is None:
            num_cases = line
            continue
        a, b = line.split()
        run_test_case(case_num, int(a), int(b))
        case_num += 1

