#!/opt/local/bin/python3.1

def calc_gcd(x, y):
    mod = y % x
    if mod == 0:
        return x
    else:
        return calc_gcd(mod, x)

C = int(input())
for c in range(1, C + 1):
    t = list(map(int, input().split()))
    n = t[0]
    t = t[1:]
    t.sort()
    diff = [t[i + 1] - t[i] for i in range(0, n - 1)]
    diff.sort()
    gcd = diff[0]
    for i in range(1, n - 1):
        if gcd == 0:
            gcd = diff[i]
        else:
            gcd = calc_gcd(gcd, diff[i])
    if t[0] % gcd == 0:
        result = 0
    else:
        result = gcd * (t[0] // gcd + 1) - t[0]
    print("Case #{}: {}".format(c, result))
