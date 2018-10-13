def break10(x, pow10):
    breaker = 10 ** pow10
    head, tail = divmod(x, breaker)
    head *= breaker
    return head, tail


def digits(n):
    return {int(_) for _ in str(n)}


def find_tidy(n):

    def find_tidy_rec(n, base=1):
        head, tail = break10(n, base)
        if head == 0:
            return n
        t, _ = divmod(tail, 10 ** (base - 1))
        # print head, t, tail
        if t < max(digits(head)):
            return find_tidy_rec(head - 1, base + 1)
        else:
            return find_tidy_rec(n, base + 1)

    return find_tidy_rec(n)


def test_mode():
    tests = [
        (132, 129),
        (1000, 999),
        (7, 7),
        (111111111111111110, 99999999999999999)
    ]

    for n, expected in tests:
        actual = find_tidy(n)
        print n, "->", actual
        assert actual == expected, "actual %d != expecte" % (actual, expected)

    exit()


if __name__ == "__main__":
    # test_mode()
    T = int(raw_input())
    for i in xrange(1, T + 1):
        n = int(raw_input())
        t = find_tidy(n)
        # print "Case #%d: %d -> %d" % (i, n, t)
        print "Case #%d: %d" % (i, t)
