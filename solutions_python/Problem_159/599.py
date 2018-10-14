def first(N, m):
    total = 0
    for x in range(1, len(m)):
        diff = m[x] - m[x-1]
        if diff < 0:
            total += -diff
    return total

def second(N, m):
    rr = []
    for x in range(1, len(m)):
        a = m[x]
        b = m[x - 1]
        ineq = (a - b) / -10
        rr.append(ineq)

    eaten = 0
    c = max(rr)
    #print(c)
    for x in range(1, len(m)):
        a = m[x]
        b = m[x - 1]
        eaten += min(b, 10 * c)
    return int(eaten)



T = int(input())
for t in range(1, T+1):
    N = int(input())
    m = [int(x) for x in input().split()]
    y = first(N, m)
    z = second(N, m)
    print("Case #{0}: {1} {2}".format(t, y, z))
