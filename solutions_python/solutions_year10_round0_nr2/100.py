def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

C = int(raw_input())
for i in range(C):
    line = raw_input()
    parts = line.split()
    N = int(parts[0])
    T = [int(t) for t in parts[1:]]
    T.sort()
    D = 0
    for j in range(N - 1):
        d = T[j + 1] - T[j]
        D = gcd(D, d)
    if T[0] % D == 0:
        y = 0
    else:
        y = D - T[0] % D
    print 'Case #%d: %d' % (i + 1, y)
