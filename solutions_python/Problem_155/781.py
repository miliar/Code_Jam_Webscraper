import sys
t = int(input())
for tc in range(1,t+1):
    b = [int(x) for x in input().split()[1]]
    ans = 0
    now = 0
    for i in range(len(b)):
        if b[i] != 0:
            if now < i:
                ans += i-now
                now = i
            now += b[i]
    print("Case #{}: {}".format(tc, ans))
