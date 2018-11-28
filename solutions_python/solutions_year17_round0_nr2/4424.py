from codejam import *


def is_tidy(str_number):
    """
    >>> is_tidy('9')
    True
    >>> is_tidy('1234')
    True
    >>> is_tidy('224489')
    True
    >>> is_tidy('1324')
    False
    """
    return str_number == ''.join(sorted(str_number))


def step(number):
    """
    >>> step(1232)
    3
    >>> step(3241)
    """
    number = list(str(number))
    length = len(number)
    last = number[0]
    result = 0
    for i, n in enumerate(number):
        if last > n:
            return int(''.join(number[i:])) + 1
        last = n


def main(max_number):
    n = long(max_number)
    while n > 0:
        sn = str(n)
        if is_tidy(sn):
            return n
        n -= step(n)


if __name__ == '__main__':
    in_filename, out_filename = 'tidy-numbers.sample.in', 'tidy-numbers.out'
    import sys
    in_filename = sys.argv[1]
    output = write_test_result(out_filename)
    next(output)
    for testcase_number, testcase in iter_test_cases(in_filename):
        last_number = main(*testcase)
        output.send((testcase_number, last_number))

    output.send((False, None))
