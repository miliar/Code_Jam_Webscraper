def solve(s,k):
    ans = 0
    for i in range(len(s)-k+1):
        if s[i] == '-':
            ans += 1
            for j in range(i,i+k):
                if s[j] == '-': s[j] = '+'
                else:  s[j] = '-'
    if all(x=='+' for x in s):
        return ans
    else: return "IMPOSSIBLE"

t = int(input())
for i in range(1,t+1):
    s,k = input().split()
    print("Case #%d: %s"%(i,str(solve(list(s),int(k)))))
