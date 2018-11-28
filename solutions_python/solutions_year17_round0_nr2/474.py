tn = int(input())

def good(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True

for t in range(1, tn + 1):
    n = list(map(int, list(input())))
    nval = int("".join(map(str, n)))
    l = len(n)
    ans = 1
    for x in range(l + 1):
        m = n[:]
        if (x < l and m[x] != 0):
            m[x] -= 1
            for y in range(x + 1, l):
                m[y] = 9
        mval = int("".join(map(str, m)))
        if good(m) and mval <= nval:
            if ans < mval:
                ans = mval
    print("Case #%d:" % t, ans)

    