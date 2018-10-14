#!/usr/bin/python -tt
# encoding: utf-8


import sys
# from math import sqrt


fair_square_palindromes = [1,
                           4,
                           9,
                           121,
                           484,
                           10201,
                           12321,
                           14641,
                           40804,
                           44944,
                           1002001,
                           1234321,
                           4008004,
                           100020001,
                           102030201,
                           104060401,
                           121242121,
                           123454321,
                           125686521,
                           400080004,
                           404090404,
                           10000200001,
                           10221412201,
                           12102420121,
                           12345654321,
                           40000800004,
                           1000002000001,
                           1002003002001,
                           1004006004001,
                           1020304030201,
                           1022325232201,
                           1024348434201,
                           1210024200121,
                           1212225222121,
                           1214428244121,
                           1232346432321,
                           1234567654321,
                           4000008000004,
                           4004009004004,
                           100000020000001,
                           100220141022001,
                           102012040210201,
                           102234363432201,
                           121000242000121,
                           121242363242121,
                           123212464212321,
                           123456787654321,
                           400000080000004]


def main():
    """Read in the specified file and print out the expected output."""
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print 'usage: ./FairAndSquare.py file'
        sys.exit(1)
    with open(filename, 'rU') as file_handle:
        casenum = int(file_handle.readline())
        for case in range(1, casenum + 1):
            print handle_case(case, [file_handle.readline()])


def handle_case(case, lines, **args):
    """Return a string containing the expected output given a single case.

    Handles the case supplied through the given case and lines and returns a
    string containing the expected output of the given input. The **args may be
    used to contain any additional input variables that may have been
    preprocessed.

    Args:
        case: Number specifying the current case number
        lines: List of input lines relevant to the case
        **args: Additional arguments (e.g. preprocessed input)

    Returns:
        A string of the expected output of the corresponding test case.
    """

    tokens = [int(x) for x in lines[0].split()]
    result = count_fairsquare(tokens[0], tokens[1])
    return 'Case #%d: %s' % (case, result)


def get_next_palindrome(x):
    """Return the next smallest palindrome number from x palindrome"""
    # Huh... writing 'useless' comments helps with coding flow...
    # turn number to string and store length for ease
    x = str(x)
    len_x = len(x)
    # length is even
    if len_x % 2 == 0:
        sp = len_x / 2
        x_half1 = x[:sp]
        # assuming x is a palindrome...
        x_half1_plus = str(int(x_half1) + 1)
        # if length is still the same... then return
        if len(x_half1) == len(x_half1_plus):
            return x_half1_plus[:] + x_half1_plus[::-1]
        else:
            return x_half1_plus[:-1] + x_half1_plus[::-1]
    else:
        sp = (len_x / 2) + 1
        x_half1 = x[:sp]
        # assuming x is a palindrome...
        x_half1_plus = str(int(x_half1) + 1)
        # if length is still the same... then return -1
        if len(x_half1) == len(x_half1_plus):
            return x_half1_plus[:] + x_half1_plus[:-1][::-1]
        else:
            return x_half1_plus[:-1] + x_half1_plus[:-1][::-1]


def is_sqrt_palindrome(i):
    i_sqrt = isqrt(i)
    if is_palindrome(str(i_sqrt)) and i_sqrt * i_sqrt == i:
        return True
    return False


# From http://code.activestate.com/recipes/577821-integer-square-root-function/
# MIT License
def isqrt(x):
    """Use Newton's method to return the isqrt of x."""
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2 ** (a + b)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


def is_palindrome(x):
    """Check if x is a palindrome."""
    sp = len(x) / 2
    if sp == 0:
        return True
    if x[:sp] == x[-sp:][::-1]:
        return True
    return False


def counter(low, high):
    """Palindrome iterator."""
    current = low
    while current <= high:
        # if str(current)[0] not in '124':
        #     str_curr = str(current)
        #     current += int(''.join(['1', '0' * (len(str_curr) - 1)]))
        current = int(get_next_palindrome(current))
        yield current


def count_fairsquare(start, end):
    """Return the number of fairsquare numbers between the interval."""
    return len([i for i in fair_square_palindromes
                if start <= i <= end])


def generate_fairsquare():
    """Generate fairsquare for the given interval."""
    for i in counter(1, 10 ** 50):
        if str(i)[0] in '124' and is_sqrt_palindrome(int(i)):
            print i, isqrt(i)


def palindrome_tests():
    print '------'
    print get_next_palindrome(1) == '2'
    print get_next_palindrome(8) == '9'
    print get_next_palindrome(9) == '11'
    print get_next_palindrome(11) == '22'
    print get_next_palindrome(99) == '101'
    print get_next_palindrome(171) == '181'
    print get_next_palindrome(191) == '202'
    print get_next_palindrome(999) == '1001'
    print get_next_palindrome(1771) == '1881'
    print get_next_palindrome(1991) == '2002'
    print get_next_palindrome(9999) == '10001'


if __name__ == '__main__':
    # palindrome_tests()
    # generate_fairsquare()
    main()
