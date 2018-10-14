t = int(input())

for tc in range(1, t+1):
    a, b = map(int, input().split())
    p = sorted([[int(x) for x in input().split()] for _ in range(a+b)])
    if max(a, b) < 2:
        print("Case #{}: {}".format(tc, 2))
        continue
    res = 2
    if p[1][0] - p[0][1] < 12*60 and p[1][1] - p[0][0] > 12*60:
        res +=2
    print("Case #{}: {}".format(tc, res))
