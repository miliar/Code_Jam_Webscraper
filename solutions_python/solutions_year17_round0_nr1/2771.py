f = open('ans.txt', 'w')
k = int(input())
for h in range(1, k+1):
    s, n = input().split()
    n = int(n)
    s = list(s)
    ans = 0
    for i in range(len(s)-n+1):
        if s[i] == '-':
            ans+=1
            for j in range(i, i+n):
                if s[j] == '-':
                    s[j] = '+'
                elif s[j] == '+':
                    s[j] = '-'
    for i in range(len(s)-n+1, len(s)):
        if s[i] == '-':
            f.write(f"Case #{h}: IMPOSSIBLE\n")
            break
    else:
        f.write(f"Case #{h}: {ans}\n")
f.close()
