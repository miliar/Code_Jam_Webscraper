import sys

#import itertools
f = open(sys.argv[1])
T = int(f.readline())
for t in range(T):
    print "Case #" + str(t + 1) + ":",
    (N, M) = f.readline().split()
    N = int(N)
    M = int(M)
    P = []

    def fn(k):
        global N
        return k * N - k * (k - 1) / 2

    for m in range(M):
        (o, e, p) = f.readline().split()
        P.append([int(o), int(e), int(p)])

    OS = 0
    for p in P:
        OS = OS + p[2] * fn(p[1] - p[0])
    S = 0
    tickets = [0] * (N + 1)
    for n in range(N + 1):
        #shift tickets
        for i in range(N - 2, -1, -1):
            tickets[i + 1] = tickets[i]
        tickets[0] = 0

        #enter passengers
        ex = 0
        for p in P:
            if p[0] == n:
                #print "Enter", p[2], "passengers"
                tickets[0] = tickets[0] + p[2]
            if p[1] == n:
                ex = ex + p[2]

        #exit passenger
        #print "Exit", ex, ",tickets = ", tickets
        i = 0
        while ex > 0 and i < N + 1:
            #print i, ":exit ", ex, "tickets", tickets[i], "S = ", S
            if ex >= tickets[i]:
                ex = ex - tickets[i]
                S = S + tickets[i] * fn(i)
                tickets[i] = 0
            else:
                tickets[i] = tickets[i] - ex
                S = S + ex * fn(i)
                ex = 0
            i = i + 1
        #print "After exit tickets = ", tickets

    for i in range(len(tickets)):
        if tickets[i] != 0:
            S = S + fn(i)

    print OS - S

