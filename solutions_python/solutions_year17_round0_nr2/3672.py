def digits(n):
    if n < 10:
        return [n]
    else:
        return digits(n//10) + [n%10]


def tidy(n):
    d = digits(n)
    for i in range(len(d) - 2, -1, -1):
        if d[i] > d[i + 1]:
            d[i] -= 1
            for j in range(i + 1, len(d)):
                d[j] = 9
    res = 0
    for i, a in enumerate(reversed(d)):
        res += a*10**i
    return res

T = int(input())
for i in range(T):
    n = int(input())
    print("Case #{}: {}".format(i + 1, tidy(n)))