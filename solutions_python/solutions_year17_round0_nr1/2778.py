def solve():
    s, k = input().split()
    k = int(k)
    s = list(s)
    cnt = 0
    for i in range(len(s)):
        if s[i] == '-':
            cnt += 1
            if i + k > len(s):
                return 'IMPOSSIBLE'
            for j in range(i, i + k):
                if s[j] == '-':
                    s[j] = '+'
                else:
                    s[j] = '-'
    return cnt


T = int(input())

for t in range(T):
    print("Case #"+str(t+1) +": " + str(solve())) 
