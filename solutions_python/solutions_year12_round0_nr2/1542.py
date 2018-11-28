def Googlers(N, S, p, t):
    if (p == 0):
        return N
    y = 0
    for ti in t:
        if (ti == 0):
            break
        if (ti < (((p - 1) * 3) - 1)):
            break
        average = ti / 3
        if (average >= p):
            y = y + 1
            continue
        if (((ti % 3) <> 0) and ((average + 1) == p)):
            y = y + 1
            continue
        if (S > 0):
            y = y + 1
            S = S - 1
        else:
            break
    return y

T = input()
for i in range(0, T):
    integers = map(int, raw_input().split())
    N = integers[0]
    S = integers[1]
    p = integers[2]
    print "Case #%s: %s" % (i + 1, Googlers(N, S, p, sorted(integers[3:], reverse = True)))
