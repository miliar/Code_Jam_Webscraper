from sys import stdin

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def solve(t):
    t.sort()
    f = 0
    for i in range(len(t) - 1):
        f = gcd(f, (t[i + 1] - t[i]))
    y = (f - t[0] % f) % f
    return y

C = int(stdin.readline())
for no in range(1, C + 1):
    tokens = stdin.readline().split()
    answer = solve(map(int, tokens[1:]))
    print "Case #%s: %s" % (no, answer)
