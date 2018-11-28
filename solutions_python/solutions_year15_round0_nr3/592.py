ONE, I, J, K = '1', 'i', 'j', 'k'

mat = {
    ONE: {ONE: ONE, I: I, J: J, K: K},
    I: {ONE: I, I: '-' + ONE, J: K, K: '-' + J},
    J: {ONE: J, I: '-' + K, J: '-' + ONE, K: I},
    K: {ONE: K, I: J, J: '-' + I, K: '-' + ONE},
}


def memoized(func):
    memo = {}

    def wrapper(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]

    return wrapper


@memoized
def mul(a, b):
    neg = 1
    if len(a) > 1:
        a = a[1]
        neg *= -1
    if len(b) > 1:
        b = b[1]
        neg *= -1

    result = mat[a][b]
    if neg < 0:
        result = '-' + result
    if len(result) > 2:
        result = result[-1]

    return result


def reduced(seq):
    if not seq:
        return None

    result = ONE
    for s in seq:
        result = mul(result, s)

    return result


def search(seq, val):
    result = ONE
    for i, s in enumerate(seq):
        result = mul(result, s)
        if result == val:
            yield i


def solve(seq):

    @memoized
    def _red(i):
        return reduced(seq[i:])

    for i in search(seq, I):
        for j in search(seq[i + 1:], J):
            if _red(i + j + 2) == K:
                return 'YES'
    return 'NO'


def test():

    assert solve('ik') == 'NO'
    assert solve('ijk') == 'YES'
    assert solve('kji') == 'NO'
    assert solve('ji' * 6) == 'YES'
    #assert solve('i' * 10000) == 'NO'


if __name__ == '__main__':
    test()
    import sys

    data = open(sys.argv[1] + '.in').readlines()
    T = int(data[0].strip())

    for i in range(T):
        l, x = map(int, data[2 * i + 1].strip().split())
        seq = x * data[2 * i + 2].strip()
        print 'Case #%i: %s' % (i + 1, solve(seq))
