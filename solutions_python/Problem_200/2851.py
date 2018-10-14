from copy import copy

T = int(raw_input())
for tt in range(T):
    N = [int(x) for x in raw_input()]
    M = copy(N)
    N.reverse()
    for i in range(len(N)-1):
        if N[i] < N[i+1]:
            N[i] = 9
            for j in range(i):
                N[j] = 9
            N[i+1] -= 1
        elif N[i] == N[i+1] == 0:
            N[i] = 9
    while N[-1] == 0:
        N.pop()
    N.reverse()
    #print M
    #print N
    #print "_-----"
    print "Case #" + str(tt+1)+": "+str("".join(map(str,N)))
