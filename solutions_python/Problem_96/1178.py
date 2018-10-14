import sys
import math

def computePossibleBestPoints(total_points):
    d = total_points / 3
    m = total_points % 3
    if d == 0:
        return [min(1,m), m]
    elif m == 0:
        return [d, d+1]
    elif m == 1:
        return [d+1, d+1]
    elif m == 2:
        return [d+1, d+2]

def DPsolve(N, S, p, dp_input):
    M = []
    for n in range(N+1):
        M.append([])
        for s in range(S+1):
            M[n].append(0)

    # initialization first column
    for n in range(1,N+1):
        M[n][0] = M[n-1][0]
        if dp_input[n-1][0] >= p:
            M[n][0] = M[n][0] + 1
            
    #  general case       
    for n in range(1,N+1):
        for s in range(1,S+1):
            # two posible movs:
            #   1) in the same column
            #   2) jumping one column
            for sp in range(2):
                v = M[n-1][s-sp]
                if dp_input[n-1][sp] >= p:
                    v = v + 1
                if v > M[n][s]:
                    M[n][s] = v
    # print M
    return M[N][S]

T = int(sys.stdin.readline())
for i in range(T):
    data = sys.stdin.readline().strip().split(" ")
    N = int(data[0]) # Number of Googlers
    S = int(data[1]) # Number of suprising triplets
    p = int(data[2]) # At least p best points
    dp_input = [computePossibleBestPoints(int(data[j])) for j in range(3,3+N)]
    print "Case #%d: %d"%((i+1),DPsolve(N, S, p, dp_input))
    
