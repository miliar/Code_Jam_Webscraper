import sys

fileName = "B-large"
sys.stdin = open(fileName+".in", 'r')
output = open(fileName+".out", 'w')
T = int(input())
for case in range(1,T+1):

    ###################### input data ###############################

    N,P = input().split(" ")
    print("N="+N+", P="+P)
    N,P = int(N),int(P)
    R = input().split(" ")
    for i in range(len(R)):
        R[i]=int(R[i])
    print("R="+str(R))

    Q = []
    for i in range(N):
        Q.append(input().split(" "))
    for i in range(N):
        for j in range(P):
            Q[i][j] = int(Q[i][j])
        Q[i].sort()
    """
    print("Q = "+str(Q))
    """

    ######################### compute answer ##################################

    answer = 0
    k=0
    finished=False
    while k<10**6 and not finished:
        k+=1
        good = True
        while good and not finished:
            for i in range(N):
                while not finished and Q[i][0]<0.9*k*R[i]:
                    Q[i].pop(0)
                    if len(Q[i])==0:
                        finished=True
                if not finished and Q[i][0]>1.1*k*R[i]:
                    good=False
            if good and not finished:
                answer+=1
                for i in range(N):
                    Q[i].pop(0)
                    if len(Q[i])==0:
                        finished=True
    answer = str(answer)

    ######################## create output file ###############################
    print("Case #%d:" % case, answer)
    print("Case #%d:" % case, answer, file = output)
    ###########################################################################
