EPS = 1e-15

def solve():
    n, k = map(int, input().split())
    u = float(input())
    p = list(map(float, input().split()))
    p.sort()
    curr = 1
    if n == 1:
        p[0] += u
        u = 0
    while u > EPS:
        #print(curr, u, p)
        if curr >= n:
            diff = u / n
            for i in range(n):
                p[i] += diff
            u = 0
        elif p[0] < p[curr] - EPS:
            diff = min(p[curr] - p[0], u/curr)
            for i in range(curr):
                p[i] += diff
            u -= curr*diff
            curr += 1
        else:
            curr += 1
    res = 1
    for i in range(n):
        res *= p[i]
    print(res)

if __name__ == '__main__':
    t = int(input())
    for tc in range(1,t+1):
        print("Case #{}: ".format(tc), end='')
        solve()
        #print('')
