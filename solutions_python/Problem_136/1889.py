#!/usr/bin/python3

def readln(): return tuple(map(int, input().split()))

def solve(case):
    c, f, x = tuple(map(float, input().split()))
    ans = 1e18
    s = 0.0
    m = 2.0
    for _ in range(10**5):
        nans = c * s + x / m
        if nans < ans:
            ans = nans
        else:
            break
        s += 1 / m
        m += f
    print('Case #%d: %0.7f' % (case, ans))

if __name__ == '__main__':
    t, = readln()
    for _ in range(t):
        solve(_ + 1)