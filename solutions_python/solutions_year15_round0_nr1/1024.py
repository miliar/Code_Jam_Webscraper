n = int(input())

def solve():
    n, inp = input().split()
    n = int(n)
    inp = list(map(int, inp))
    ans = 0
    cur = inp[0]
    for i in range(1, len(inp)):
        if inp[i] and i > cur:
            ans += i - cur
            cur += ans
        cur += inp[i]
    return ans

for i in range(n):
    print("Case #%d: %d" % (i+1, solve()))
