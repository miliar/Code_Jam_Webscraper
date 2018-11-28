def split(n):
    x = int(n / 2)
    if n % 2 == 0:
        return x, x - 1
    else:
        return x, x

def f(n, k):
    l = 0
    r = 0
    gaps = [n]
    while k > 0:
        m = max(gaps)
        l, r = split(m)
        gaps.remove(max(gaps))
        gaps.append(l)
        gaps.append(r)
        k = k - 1
    return l, r

t = int(input())
for i in range(1, t + 1):
    stalls, people = [int(s) for s in input().split(" ")]
    a, b = f(stalls, people)
    print("Case #{}: {} {}".format(i, a, b))
