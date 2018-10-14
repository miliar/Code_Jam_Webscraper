def solve(s, k, n):
    count = 0
    s_size = len(s)
    for i in range(s_size-k+1):
        if s[i] == "-":
            tmp = ""
            for j in range(k):
                if s[i+j] == "-":
                    tmp += "+"
                else:
                    tmp += "-"
            s = s[:i] + tmp + s[i+k:]
            count += 1
    
    if "-" in s[s_size-k:s_size]:
        print("Case #{}: IMPOSSIBLE".format(n+1))
    else:
        print("Case #{}: {}".format(n+1, count ))


t = int(input())
for i in range(t):
    s, k = input().split()
    k = int(k)
    solve(s, k, i)