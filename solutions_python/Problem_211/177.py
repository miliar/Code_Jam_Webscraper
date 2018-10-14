# 0th solution to Problem C

t = int(input())

def solve():
    n, k = map(int, input().split(' '))
    u = float(input())
    p = list(map(float, input().split(' ')))
    if len(p) == 1:
        return min(p[0]+u, 1.0)

    p = sorted(p)

    while u > 0:
       # print(p)
        #print(u)
        failed = True
        ind = None
        for i, x in enumerate(p):
            if x != p[0]:
                failed = False
                ind = i
                diff = (x - p[0])*ind
                break
        if failed:
            for i in range(len(p)):
                p[i] += u/len(p)
                if p[0] >= 1.0:
                    return 1.0
            break

        else:
            if diff < u:
                u -= diff
                for i in range(ind):
                    p[i] = p[ind]

            else:
                for i in range(ind):
                    p[i] += u/ind
                if p[0] >= 1.0:
                    return 1.0
                u = 0.0

    res = 1.0
    for pr in p:
        res *= pr
    return res

for a0 in range(t):
    sol = solve()
    sol = '{:.35f}'.format(sol)
    print("Case #" + str(a0 + 1) + ": " + sol)
