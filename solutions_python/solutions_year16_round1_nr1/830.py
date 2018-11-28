import itertools
import math
import sys

def main():
    num_cases = int(sys.stdin.readline())

    line_num = 1
    for line in sys.stdin:
        line = line.strip()

        solution = compute(line)
        assert_is_string(solution)

        print 'Case #%d: %s' % (line_num, solution)

        line_num += 1

    assert num_cases == line_num - 1


def assert_is_numeric(n):
    assert type(n) in [int, long]


def assert_is_string(s):
    assert isinstance(s, basestring)


def assert_is_numeric_list(arr):
    for n in arr:
        assert_is_numeric(n)


def assert_is_bool_list(arr):
    for b in arr:
        assert type(b) is bool


def test():
    yield


def compute(s):
    '''  '''
    ret = ''
    for char in s:
        if not ret:
            ret += char
        else:
            if ret[0] <= char:
                ret = char + ret
            else:
                ret = ret + char
    return ret


if __name__ == '__main__':
    test()
    #print 'All tests passed'
    main()