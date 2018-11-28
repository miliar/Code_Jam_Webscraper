t = int(input())

for tc in range(t):
    d, n = [int(x) for x in input().split()]
    horses = []
    for _ in range(n):
        p, s = [int(x) for x in input().split()]
        horses.append((d-p)/s)
    print('Case #{}: {:.6f}'.format(str(tc+1), d/max(horses)))
