'''
Created on Apr 13, 2013

@author: steve
'''

def possible(a, N, M):
    if N == 0 or M == 0: return True
    
    m = a[0][0]
    mini = 0
    minj = 0
    for i in range(N):
        for j in range(M):
            if a[i][j] < m:
                m = a[i][j]
                mini = i
                minj = j
    
    # Check horizontal stripe
    hstripe = True
    for j in range(M):
        if a[mini][j] != m:
            hstripe = False
    if hstripe:
        return possible([a[i] for i in range(N) if i != mini], N-1, M)
    
    # Check for vertical stripe
    vstripe = True
    for i in range(N):
        if a[i][minj] != m:
            vstripe = False
    if vstripe:
        return possible([[a[i][j] for j in range(M) if j != minj]  for i in range(N)], N, M-1)
    else:
        return False

T = int(input())

for Ti in range(1,T+1):
    N, M = [int(i) for i in input().split(' ')]
    a = [[int(i) for i in j] for j in [input().split(' ') for l in range(N)]]
    print('Case #%d: ' % Ti, end='')
    if possible(a, N, M):
        print('YES')
    else:
        print('NO')