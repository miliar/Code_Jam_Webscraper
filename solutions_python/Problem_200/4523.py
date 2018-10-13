
def solution(t):
    c = 1
    d = 0
    if t < 10:
        return t
    while c < t:
        c *= 10
        d += 1
    if c == t:
        return c - 1
    else:
        d -= 1
        c /= 10
        last = t// c
        n = t - c * last
        new_n = 0
        while d > 1:

            d -= 1
            c /= 10
            f = n // c
            if f < last:
                new_n += (last - 1) * c * 10
                return new_n + c * 10 - 1
            else:
                new_n += c * 10 * last
                last = f
                n -= c * last
        c /= 10
        f = n // c
        if f < last:
            new_n += (last - 1) * c * 10
            new_n += c * 10 - 1
            return new_n
        else:
            return t


def solution2(t):
    if t < 10:
        return t
    d = 1
    c = 10
    b = 0
    last = t % c
    rest = t // c
    new_n = last
    while rest > 10:
        f = rest % 10
        if f <= last:
            last = f
            rest = rest // 10
        else:
            new_n = f * (10) ** (d) - 1
            b = d
            last = f - 1
            rest = rest // 10

        d += 1
    f = rest
    if f <= last:
        return t // (10 ** (b + 1)) * (10 ** (b + 1)) + new_n
    else:
        new_n = f * (10) ** (d) - 1
        return new_n


T = int(input())

for p in range(T):
    t = int(input())
    print("Case #" + str(p + 1) + ": ", end="")
    res = solution2(t)
    print(int(res))
