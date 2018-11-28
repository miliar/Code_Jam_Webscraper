import sys

def is_sorted(digits):
    x = -1
    for d in digits:
        if d < x:
            return False
        x = max(x, d)
    return True

def ss(digits):
    return ''.join(str(d) for d in digits)

def try_next(digits):
    i = len(digits)-1
    while digits[i] == 9:
        i -= 1
        if i < 0:
            return digits
    digits[i] = 9
    i -= 1
    while True:
        if digits[i] > 1:
            digits[i] -= 1
            return digits
        if digits[i] == 1:
            digits[i] = 0
            if i == 0:
                return digits[1:]
            return digits
        if digits[i] == 0:
            digits[i] = 9
            i -= 1

    return digits


def solve(N):
    digits = [int(c) for c in str(N)]
    while True:
        if is_sorted(digits):
            return ss(digits)
        digits = try_next(digits)


def main():
    T = int(sys.stdin.readline().strip())

    for i in xrange(T):
        N = int(sys.stdin.readline())
        ans = solve(N)
        print 'Case #%s: %s' % (i+1, ans)

if __name__ == '__main__':
    main()
