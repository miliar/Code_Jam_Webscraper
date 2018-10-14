n = int(input())

def solve():
    s, k = input().split()
    k = int(k)
    s = [x == '-' for x in s]
    cnt = 0
    for i in range(len(s) - k + 1):
        if s[i]:
            for j in range(k):
                s[i+j] ^= True
            cnt += 1
    if any(s):
        return "IMPOSSIBLE"
    else:
        return cnt


for i in range(1, n+1):
    print("Case #%d:" % i, solve())
