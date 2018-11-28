MIN_LENGTH = 1
MAX_LENGTH = 14


def all_palindromes():
    result = set(range(10))
    for i in xrange(1, 9999999):
        val = str(i)
        result.add(val + val[::-1])
        result.add(val + val[:-1][::-1])
    return result


def gen_all_fair_square():
    return set([
        1, 1020304030201, 4, 1000002000001, 9, 14641, 4000008000004,
        44944, 1002001, 121, 1214428244121, 12102420121,
        4004009004004, 1004006004001, 404090404, 40000800004,
        12345654321, 10000200001, 1234321, 1234567654321,
        1210024200121, 121242121, 40804, 1232346432321, 4008004,
        100020001, 1022325232201, 125686521, 10201, 123454321,
        400080004, 484, 12321, 1002003002001, 1212225222121,
        1024348434201, 104060401, 10221412201, 102030201
    ])

    fair_square = set([])
    palins = all_palindromes()
    for palin in palins:
        sqr = int(palin) ** 2

        if str(sqr) in palins:
            fair_square.add(sqr)

    return fair_square


if __name__ == "__main__":
    T = int(raw_input())
    fair_square = gen_all_fair_square()

    for t in xrange(T):
        A, B = map(int, raw_input().split())
        result = 0
        for value in fair_square:
            if A <= value <= B:
                result += 1
        print "Case #%d: %d" % (t + 1, result)
