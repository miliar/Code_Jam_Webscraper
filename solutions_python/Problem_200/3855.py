import sys


class InputFileParser(object):
    def __init__(self, filename):
        self.test_cases = []
        with open(filename, 'r') as in_f:
            self.test_case_count = int(in_f.readline())
            for i in xrange(1, self.test_case_count + 1):
                tc = TestCase(i)
                tc.last = int(in_f.readline())
                self.test_cases.append(tc)


class TestCase(object):
    def __init__(self, index):
        self.index = index
        self.last = 0
        self.result = 0


def to_digits(number):
    return map(lambda digit_str: int(digit_str), str(number))


def to_number(digits):
    return int(''.join(map(str, digits)))


def drop_last(digits):
    result = digits[:-1]
    result[-1] = result[-1] - 1
    return result


def is_tidy(digits):
    previous = 0
    for digit in digits:
        if digit < previous:
            return False
        previous = digit
    return True


def last_tidy(last):
    left = to_digits(last)
    right = []
    while not is_tidy(left):
        right.append(9)
        left = drop_last(left)
    return to_number(left + right)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit('input and output file not specified!')

    parser = InputFileParser(sys.argv[1])
    with open(sys.argv[2], 'w') as out_f:
        for tc in parser.test_cases:
            tc.result = last_tidy(tc.last)
            print 'Case #{0}: {1}'.format(tc.index, tc.result)
            out_f.write('Case #{0}: {1}\n'.format(tc.index, tc.result))
