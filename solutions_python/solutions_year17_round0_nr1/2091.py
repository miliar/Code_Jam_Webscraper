def solve(n):
    s,k = n.split()
    s = list(s)
    k = int(k)

    ans = 0

    for i in range(len(s)):
        if s[i] == '+':
            continue
        if k > (len(s) - i):
            return "IMPOSSIBLE"
        for j in range(k):
            s[i+j] = flip(s[i+j])
        ans += 1
    return ans

def flip(c):
    return '-' if c=='+' else '+'

t = int(input())
for i in range(t):
    print("Case #{0}: {1}".format(i+1, solve(input())))