import sys


def pal(a):
    s = str(a)
    n = len(s)
    if n % 2 == 0:
        return s[:n / 2] == s[n / 2:][::-1]
    else:
        return s[:n / 2] == s[-1:n / 2:-1]

def num_fair_and_square(a, b):
    result = 0
    n = 1
    while True:
        n2 = n * n
        if n2 >= a:
            break
        n += 1
    while True:
        n2 = n * n
        if n2 > b:
            break
        if pal(n2) and pal(n):
            result += 1
        n += 1
    return result


if __name__ == '__main__':
    TESTS = int(sys.stdin.readline())
    for z in range(1, TESTS + 1):
        a, b = [int(x) for x in sys.stdin.readline().split()]
        result = num_fair_and_square(a, b)
        print("Case #%d: %d" % (z, result))
