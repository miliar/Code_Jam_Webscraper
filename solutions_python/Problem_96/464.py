from sys import stdin

n_cases = int(stdin.readline())
for i in range(n_cases):
    kase = stdin.readline().split()
    kase = [int(z) for z in kase]
    S = kase[1]
    p = kase[2]
    kase = kase[3:]

    a = p + 2 * max(p - 1, 0)
    b = p + 2 * max(p - 2, 0)
    c = len(filter(lambda k: a <= k, kase))
    d = len(filter(lambda k: b <= k < a, kase))
    e = c + min(d, S)

    print "Case #{}: {}".format(i + 1, e)
