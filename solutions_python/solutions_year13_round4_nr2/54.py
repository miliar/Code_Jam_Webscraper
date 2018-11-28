import sys

def alwaysWin(n, p, k):
    if n == 0:
        return True
    if k == 0:
        return True
    if p <= 2 ** (n - 1):
        return False
    return alwaysWin(n - 1, p - 2 ** (n - 1), (k - 1) / 2)

def canWin(n, p, k):
    if n == 0:
        return True
    if p >= 2 ** n:
        return True
    if k == 0:
        return False
    if p >= 2 ** (n - 1):
        return True
    return canWin(n - 1, p, (k - 1) / 2)

def solve(test):
    n, p = [int(_) for _ in sys.stdin.readline().split()]
    L = 0
    R = (2 ** n)
    while R - L > 1:
        Q = (L + R) / 2
        if alwaysWin(n, p, Q):
            L = Q
        else:
            R = Q

    first = L

    L = 0
    R = (2 ** n)
    while R - L > 1:
        Q = (L + R) / 2
        if canWin(n, p, (2 ** n) - Q - 1):
            L = Q
        else:
            R = Q

    second = L

    print 'Case #{0}: {1} {2}'.format(test, first, second)

def main():
    T = int(sys.stdin.readline().strip())
    for test in range(1, T + 1):
        solve(test)

main()
