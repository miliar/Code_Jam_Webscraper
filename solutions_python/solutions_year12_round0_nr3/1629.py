def rec(n, m):
    if n < 12 or m < 12:
        return False
    n = str(n)
    m = str(m)
    l = len(n)
    for i in range(l - 1, 0, -1):
        dump = ''
        dump += m[i:]
        dump += m[:i]
        if n == dump:
            return True
    return False

T = int(raw_input())
for i in range(1, T + 1):
    A, B = raw_input().split()
    A, B = int(A), int(B)
    res = 0
    for n in range(A, B + 1):
        for m in range(n + 1, B + 1):
            if rec(n, m):
                res += 1
    print "Case #" + str(i) + ": " + str(res)