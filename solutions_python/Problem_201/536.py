# Google Code Jam Contest
# @L01cDev
# Author: Loic Boyeldieu
# Date: 08-04-2017
def solve(N, K):
    if K==1:
        if N%2==0:
            return [N/2, (N/2)-1]
        else:
            return [(N-1)/2, (N-1)/2]


    if N%2==0:
        if (K-1)%2==0:
            return solve((N/2)-1, (K-1)/2)
        else:
            return solve((N/2), (K)/2)
    else:
        if (K-1)%2==0:
            return solve((N-1)/2, (K-1)/2)
        else:
            return solve((N-1)/2, K/2)

T = int(raw_input())
for i in range(1, T + 1):
    N, K = [int(j) for j in raw_input().split(" ")]
    r1, r2 = solve(N, K)
    print("Case #{}: {} {}".format(i, r1, r2))
