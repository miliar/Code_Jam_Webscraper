import sys

sys.stdin = open('A-large.in', 'r')
sys.stdout = open('A-large.out', 'w')


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
T = int(input())  # read a line with a single integer
for i in range(1, T + 1):
    D, N = [int(c) for c in input().split(" ")]
    K=[]
    S=[]
    tmax=0
    for j in range(1, N+1):
        Ki, Si = [int(c) for c in input().split(" ")]
        K.append(Ki)
        S.append(Si)
    for j in range(N):
        time = (D-K[j])/S[j]
        if time>tmax:
            tmax=time
    print("Case #{}: {}".format(i, D/tmax))
