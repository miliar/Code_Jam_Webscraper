from math import sqrt


def main():
    n = int(raw_input())
    for i in xrange(n):
        low, high = map(int, raw_input().split(' '))
        print 'Case #%d:' % (i + 1), solve(low, high)


def solve(low, high):
    return sum(is_fairsquare(n) for n in xrange(low, high + 1))


def is_fairsquare(n):
    r = sqrt(n)
    if r != int(r):
        return False
    return is_fair(int(r)) and is_fair(n)


def is_fair(n):
    s = str(n)
    return s == s[::-1]

if __name__ == '__main__':
    main()
