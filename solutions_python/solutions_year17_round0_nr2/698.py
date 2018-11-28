def _get_breaking_point(digits):
    for i in xrange(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            return i
    return len(digits) - 1


def _get_reducing_point(digits):
    ret = 0
    for i in xrange(1, len(digits)):
        if digits[i] != digits[i - 1]:
            ret = i
    return ret


def solve(number):
    digits = [int(c) for c in str(number)]
    break_point = _get_breaking_point(digits)
    if break_point != len(digits) - 1:
        to_reduce = digits[:break_point + 1]
        reducing_point = _get_reducing_point(to_reduce)
        digits[reducing_point] -= 1
        for i in xrange(reducing_point + 1, len(digits)):
            digits[i] = 9
    return int(''.join(str(x) for x in digits))


if __name__ == '__main__':
    for ts in xrange(int(raw_input())):
        print 'Case #{}: {}'.format(ts + 1, solve(int(raw_input())))
