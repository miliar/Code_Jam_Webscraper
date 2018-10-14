def ok(i):
    l = list(str(i))
    m = len(l)
    for j in range(m - 1):
        if l[j] > l[j + 1]:
            return False
    return True


def f(n):
    for i in range(n, 0, -1):
        if ok(i):
            return i


T = input()
T = int(T)
for t in range(1, T + 1):
    n = input()
    n = int(n)
    res = f(n)
    print("Case #" + str(t) + ": " + str(res))
