def solve(A,B,K):
    count = 0
    for i in range(0,A):
        for j in range(0,B):
            if (i&j < K): count = count + 1
    return count
    





'''def comp(a,b,k,pos):
    if (len(k)) == 0: '''

with open("B-output.txt", "w") as output:
    with open("B-small-attempt0.in", "r") as input:
        N = int(input.readline().strip())
        for i in range (0,N):
           A,B,K = map(int, input.readline().strip().split())
           print ('Case #' + str(i+1) + ': ' + str(solve(A,B,K)),file=output)