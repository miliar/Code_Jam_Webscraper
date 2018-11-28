def solve(s, k):
    ans = 0
    for i in range(len(s)-k+1):
        if s[i] < 0:
            ans += 1
            for j in range(k):
                s[i+j] *= -1
    
    if len(s) != sum(s):
        return 'IMPOSSIBLE'
    return ans

import sys
sys.stdin = open('in.txt')
sys.stdout = open('out.txt', 'w')
q=int(input())
for i in range(q):
    s,k = input().split()
    s = list(map(lambda c: -1 if c == '-' else 1, list(s)))
    print('Case #{:d}:'.format(i+1), solve(s, int(k)))
sys.stdin.close()
sys.stdout.close()