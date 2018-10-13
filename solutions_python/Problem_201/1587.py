import sys
    
def c(N, K):
    if K == N:
        return 0, 0
    if K == 1:
        return (N-1)//2, N//2

    #return c(N//2, K//2)
    m1, M1 = c(N//2, K//2)
    if (K == 2):
        return m1, M1
    
    m2, M2 = c((N-1)//2, (K-1)//2)

    if m1 < m2:
        return m1, M1
    elif m1 == m2:
        if M1 < M2:
            return m1, M1
        else:
            return m2, M2
    else:
        return m2, M2

n = int(input())
for i in range(n):
    line = input()
    li = line.split();
    
    N = int(li[0])
    K = int(li[1])

    m, M = c(N, K)
    
    print('Case #' + str(i + 1) + ': ', end='')
    print(str(M) + ' ' + str(m))

    
