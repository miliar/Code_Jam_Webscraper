t = int(input())


def done(n):
    for i in range(len(n)):
        if i == 0:
            continue
        elif n[i] < n[i - 1]:
            return False
    return True


def cut(n, i):
    n = decrease(n, i - 1)
    for j in range(i, len(n)):
        n[j] = 9
    return n


def decrease(n, i):
    n[i] -= 1
    if n[i] == -1:
        n[i] = 9
        return decrease(n, i - 1)
    else:
        return n


for c in range(t):
    n = [int(i) for i in list(input())]

    for i in range(len(n)-1, 0, -1):
        if n[i] < n[i-1]:
            n = cut(n, i)

    out = 0
    for i in n:
        out *= 10
        out += i
    print("Case #%d: %d" % (c + 1, out))
