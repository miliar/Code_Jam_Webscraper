t = int(raw_input())


def getTidy(n):
    f = n[0]
    s = f + ("0" * (len(n) - 1))
    s = int(s)
    e = f * (len(n))
    e = int(e)
    x = int(n)

    if x == e:
        return n
    if e > x:
        return str(s-1)
    return n[0] + getTidy(n[1:])
    

for i in range(t):
    n = str(raw_input())
    print "Case #{}: {}".format(i+1, getTidy(n))

