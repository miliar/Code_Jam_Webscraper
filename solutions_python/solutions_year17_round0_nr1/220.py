
def solve():
    s, k = input().split()
    k = int(k)
    s = list(s)
    ans = 0
    for i in range(len(s)-k+1):
        if s[i]=='-':
           ans += 1
           for j in range(i,i+k):
               s[j]='+' if s[j]=='-' else '-'
    if ''.join(s[-k:])==('+'*k):
        return ans
    return 'IMPOSSIBLE'

T = int(input())
for _ in range(T):
    print('Case #%d:'%(_+1),solve())
