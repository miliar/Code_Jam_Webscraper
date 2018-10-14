from math import ceil


def main2(n, l):
    l = [i % 2 for i in l]
    a = l.count(0)
    b = l.count(1)
    return a + b // 2 + b % 2


def main3(n, l):
    l = [i % 3 for i in l]
    a = l.count(0)
    b = l.count(1)
    c = l.count(2)
    b, c = min(b, c), max(b, c)
    return a + b + ceil((c - b) / 3)


for t in range(int(input())):
    n, p = map(int, input().split())
    l = map(int, input().split())
    if p == 2:
        ans = main2(n, l)
    elif p == 3:
        ans = main3(n, l)
    print("Case #%s: %s" % (t + 1, ans))
