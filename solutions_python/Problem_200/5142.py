def last_tidy(n, case):
    length = len(n)
    num = int(n)
    for cool in xrange(num, 0, -1):
        ok = is_tidy(cool, length)
        if ok:
            print "Case #{}: {}".format(case+1, cool)
            return


def is_tidy(s, length):
    first = get_digit(s, 0)
    for a in xrange(1, length):
        second = get_digit(s, a)
        if first < second:
            return False
        first = second
    return True


def get_digit(number, n):
    return number // 10**n % 10

t = raw_input()
t = int(t)
for case in xrange(0, t):
    i = raw_input()
    last_tidy(i, case)
