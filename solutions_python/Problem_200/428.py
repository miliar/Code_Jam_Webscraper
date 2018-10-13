def is_tidy(s):
    for i in xrange(len(s) - 1):
        if s[i] > s[i + 1]:
            return False

    return True


def subtract_one(s):
    if s == '1':
        return ''

    if s[-1] > '0':
        return s[:-1] + str(int(s[-1]) - 1)

    return subtract_one(s[:-1]) + '9'


def find_largest_tidy(s):
    s = s.lstrip('0')
    while not is_tidy(s):
        for i in xrange(1, len(s) + 1):
            if not is_tidy(s[:i]):
                s = subtract_one(s[:i] + ('0' * len(s[i:])))
                break

    return s


def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        s = raw_input()
        print 'Case #%d: %s' % (i, find_largest_tidy(s))

if __name__ == '__main__':
    main()
