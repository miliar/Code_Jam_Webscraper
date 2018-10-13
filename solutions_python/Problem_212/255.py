def solve():
    N,P = [int(v) for v in input().split()]
    arr = [int(v) for v in input().split()]
    if P==2:
        mod = [0,0]
        for v in arr:
            mod[v%P] += 1
        return N-mod[1]//2
    if P==3:
        mod = [0,0,0]
        for v in arr:
            mod[v%P] += 1
        m = min(mod[1],mod[2])
        cnt = m
        mod[1] -= m
        mod[2] -= m
        return mod[0] + cnt + (max(mod[1],mod[2])+2)//3
    return -1

T = int(input())
for t in range(1, T + 1):
    print('Case #%d:' % t, solve())


