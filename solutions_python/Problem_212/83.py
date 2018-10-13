import collections
def solve(N, P, G):
    count = collections.Counter([g%P for g in G])
    if P == 2:
        return count[0]+(count[1]+1)//2
    if P == 3:
        bs = min(count[1], count[2])
        rm = max(count[1], count[2])-bs
        return count[0]+bs+(rm+2)//3
    return str(count)

cnt = int(input())
for i in range(cnt):
    N, P = [int(j) for j in input().split(' ')]
    G=[int(j) for j in input().split(' ')]
    print('Case #' + str(i+1) +': '+str(solve(N, P, G)))