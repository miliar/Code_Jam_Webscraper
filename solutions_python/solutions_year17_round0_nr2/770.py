def ok(x):
    return x == sorted(x)


def test():
    x = list(map(int, list(input())))
    res = -1
    for i in range(len(x)):
        spr = x[:i] + [x[i]-1] + [9]*(len(x)-i-1)
        if ok(spr):
            res = max(res, int("".join(map(str, spr))))
    if ok(x):
        res = max(res, int("".join(map(str, x))))
    return res


t = int(input())
for tti in range(t):
    print("Case #"+str(tti+1)+": ", test())
