from sys import stdin, stdout
from math import sqrt

stdin = open('C-large-2.in', 'r')
stdout = open('C-large-2.out', 'w')

pal2 = []

# num for current number array
# p for current production
# k for current bit index
# m for maxmum bit

num = []

def dfs(p, k, m):
    #print('num = %d, p = %d' % (int(''.join(str(x) for x in num[:-1]+num[::-1])), p))
    if k == m:
        return
    if p > 9:
        return
    if num[0] == 0 and k > 0:
        return
    if num[k] > 0:
        ans = int(''.join(str(x) for x in num[:-1]+num[::-1]))
        pal2.append(ans*ans)
    dfs(p, k+1, m)
    num[k] += 1
    dfs(p+(2*num[k]-1) * (2 if k<m-1 else 1), k, m)
    num[k] -= 1

def dfs2(p, k, m):
    if k == m:
        return
    if p > 9:
        return
    if num[0] == 0 and k > 0:
        return
    if num[k] > 0:
        ans = int(''.join(str(x) for x in num+num[::-1]))
        pal2.append(ans*ans)
    dfs2(p, k+1, m)
    num[k] += 1
    dfs2(p+(2*num[k]-1)*2, k, m)
    num[k] -= 1

for n in range(1, 27):
    num = [0] * n
    dfs(0, 0, n)
    dfs2(0, 0, n)
    

def count_pal2(x):
    cnt = 0
    while cnt < len(pal2) and pal2[cnt] <= x:
        cnt += 1
    return cnt

T = int(stdin.readline().strip())

for t in range(1, T+1):

    (A, B) = [int(x) for x in stdin.readline().strip().split()]

    x = int(sqrt(A-1))+1
    cnt = count_pal2(B) - count_pal2(A-1)

    stdout.write('Case #%d: %d\n' % (t, cnt))

stdin.close()
stdout.close()
