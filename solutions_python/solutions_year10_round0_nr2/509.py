import sys
C = input()
def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

for case in range(C):
    sys.stdout.write('Case #%d: ' % (case + 1))
    t = map(int, raw_input().split())
    N, t = t[0], t[1:]
    ans = -1
    for i in range(N - 1):
        if t[i + 1] != t[i]:
            if ans == -1:
                ans = abs(t[i + 1] - t[i])
            else:
                ans = gcd(ans, abs(t[i + 1] - t[i]))
    out = ans - t[0] % ans
    if out == ans:
        print 0
    else:
        print out
