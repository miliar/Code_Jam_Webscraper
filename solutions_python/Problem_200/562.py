import sys


def solve(source_number_str):
    """
    >>> solve('132')
    '129'
    >>> solve('1000')
    '999'
    >>> solve('7')
    '7'
    >>> solve('999777555')
    '899999999'
    >>> solve('899777555')
    '889999999'
    >>> solve('888777555')
    '799999999'
    >>> solve('999777551')
    '899999999'
    >>> solve('11110')
    '9999'
    >>> solve('111109')
    '99999'
    >>> solve('111108')
    '99999'
    >>> solve('111101')
    '99999'
    >>> solve('111100')
    '99999'
    >>> solve('111111')
    '111111'
    >>> solve('111112')
    '111112'
    >>> solve('111123')
    '111123'
    >>> solve('111233')
    '111233'
    >>> solve('113322')
    '112999'
    >>> solve('113332')
    '112999'
    >>> solve('113330')
    '112999'
    >>> solve('223330')
    '222999'
    >>> solve('323330')
    '299999'
    >>> solve('329330')
    '299999'
    >>> solve('392330')
    '389999'
    >>> solve('111111111111111110')
    '99999999999999999'
    >>> solve('111111111111111111111111111111110')
    '99999999999999999999999999999999'
    """
    number_lst = list(map(int, source_number_str))
    walk_until = len(number_lst)
    while True:
        prev_digit = 0
        for idx in xrange(walk_until):
            if prev_digit > number_lst[idx]:
                walk_until = idx
                for idx in xrange(idx - 1, -1, -1):
                    if number_lst[idx] > 0:
                        number_lst[idx] -= 1
                        break
                    elif idx > 0:
                        number_lst[idx] = 9
                    else:
                        return '9' * (len(number_lst) - 1)
                break
            prev_digit = number_lst[idx]
        else:
            break
    number_lst[walk_until:] = [9] * (len(number_lst) - walk_until)
    return ''.join(map(str, number_lst)).lstrip('0')


def main():
    count = int(next(sys.stdin).strip())
    for case in xrange(1, count + 1):
        line = next(sys.stdin).strip()
        print 'Case #{}: {}'.format(case, solve(line))


if __name__ == '__main__':
    main()
