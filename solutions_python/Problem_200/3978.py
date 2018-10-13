def solve(n):
    s = str(n)
    l = len(s)
    a = [0] * l
    for i in range(l):
        a[i] = int(s[i])

    for i in range(l-1):
        m = min(a[i+1:])
        if m >= a[i]:
            continue
        if a[i+1] > a[i]:
            continue
        a[i] -= 1
        for j in range(i+1, l):
            a[j] = 9
        break

    ret = ""
    for i in range(l):
        if i == 0 and a[i] == 0:
            continue
        ret += str(a[i])
    return ret

t = int(input())
for i in range(1, t + 1):
    n = int(input())

    ret = solve(n)
    print ("Case #%d: %s" % (i, ret))

