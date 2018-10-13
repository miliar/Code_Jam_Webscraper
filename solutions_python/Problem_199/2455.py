import numpy as np

def flip (S,K):
    N = len(S)
    K = int(K)
    A = np.empty(N,dtype=bool)
    for i in range(N):
        if S[i] == '+':
            A[i] = True
        else: 
            A[i] = False

    flips = 0

    for i in range(N):
        if i <= N-K and A[i]==False:
            A[i:i+K] = ~A[i:i+K]
            flips +=1
        elif i > N-K and A[i]==False:
            return 'IMPOSSIBLE'
    return flips


T = int(input())

for i in range(1,T+1):
    S, K = [s for s in input().split(' ')]
    print ("Case #{}: {}".format(i,flip(S,K)))