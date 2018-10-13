from itertools import count


def yield_cases(f):
    while True:
        a, b = f.next().strip().split()
        yield int(a), int(b)


def gen_palindrome():
    ''' Recursively generate all palindromic numbers. '''
    # basic building blocks of all palindromic numbers
    for i in xrange(1, 10):
        yield i

    for i in xrange(11, 100, 11):
        yield i

    pals = gen_palindrome()
    while True:
        n = pals.next()
        for i in range(1, 10) + range(11, 100, 11):
            yield int(''.join([str(n), str(i), str(n)]))  # rock on


def round10(largest):
    n = 10
    while n < largest:
        n *= 10
    return n-1


def palindrome(n):
    return str(n) == str(n)[::-1]


def create_data(large):
    data = {}
    limit = round10(large)
    pals = gen_palindrome()

    pal = pals.next()
    while pal != limit:
        if palindrome(pal ** 2):
            data[pal] = pal ** 2
        pal = pals.next()
    return data


if __name__ == "__main__":
    filename = 'test.in'
    f = open(filename)
    c = count(1)
    with f:
        n = int(f.next())
        cases = yield_cases(f)
        for small, large in cases:
            data = create_data(large)
            out = list(ifilter(lambda x: small <= x <= large, data.values()))
            print "Case #{}: {}".format(c.next(), len(out))
