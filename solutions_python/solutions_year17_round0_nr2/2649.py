import sys

T = int(sys.stdin.readline())

def check(n):
    if n < 100:
        z1 = n // 10
        z2 = n % 10
        return z1 <= z2
    else:
        z1 = (n % 100) // 10
        z2 = n % 10
        return check(n // 10) and z1 <= z2

for t in range(0, T):
    N = int(sys.stdin.readline())
    buf = 0
    ans = None
    while True:
        if check(N):
            ans = (N + 1) * (10 ** buf) - 1
            break
        else:
            N = (N // 10) - 1
            buf += 1
    print('Case #%d: %d' % (t+1, ans))

