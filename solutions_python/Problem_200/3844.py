import sys


def solve(n):
    digits = list(int(d) for d in str(n))
    l = len(digits)
    if l < 2:
        return n
    for i in xrange(l - 1):
        if digits[i] > digits[i + 1]:
            for j in xrange(i + 1, l):
            	digits[j] = 9
            digits[i] -= 1
            for j in xrange(i):
                if i - j > 0 and digits[i - j - 1] > digits[i - j]:
                    digits[i - j] = 9
                    digits[i - j - 1] -= 1
                else:
                    break
            break
    return int(''.join(str(d) for d in digits))


t = int(sys.stdin.readline())
for i in xrange(1, t + 1):
    n = int(sys.stdin.readline())
    r = solve(n)
    print 'Case #{}: {}'.format(i, r)
