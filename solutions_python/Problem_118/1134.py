import sys


def getPalindromes():
    res = []
    for i in xrange(1, 1001):
        n = str(i)
        if n == n[::-1]:
            res.append(i)
    return res


def solve(palindromes, a, b):
    count = 0
    for x in palindromes:
        n = x * x
        if n in palindromes and a <= n <= b:
            count += 1
    return count



def main(f):
    _t = int(f.readline())
    palindromes = getPalindromes()
    for t in xrange(0, _t):
        a, b = map(int, f.readline().split())
        print 'Case #%d: %d' % (t + 1, solve(palindromes, a, b))


if __name__ == '__main__':
    f = sys.stdin
    main(f)
