import sys

def input():
    T = int(sys.stdin.readline())
    for i in range(1,T+1):
        N = int(sys.stdin.readline())
        M = map(int, sys.stdin.readline().split())
        print "Case #{}: {}".format(i,count(N,M))

def count(N,M):
    sum1 = 0
    sum2 = 0
    maxi = -1
    for i,m in enumerate(M[1:], start=1):
        if M[i] < M[i-1]:
            diff = M[i-1] - M[i]
            sum1 += diff
            if diff > maxi:
                maxi = diff


    if maxi != -1:
        for i in M[:-1]:
            # print min(i,maxi)
            sum2 += min(i,maxi)
    else:
        sum2 = 0

    return "{} {}".format(sum1, sum2)



input()