import sys
t = int(input())
for tc in range(1,t+1):
    n = input()
    b = [int(x) for x in input().split()]
    ans = 0
    best = max(b)
    b.sort(reverse=True)
    for i in range(1, max(b)):
        ok = True
        specials = 0
        for x in b:
            specials += (x-1)//i
        best = min(best, i + specials)
    print("Case #{}: {}".format(tc, best))
