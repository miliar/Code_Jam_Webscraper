T= int(input())

for case in range(T):
    line=input().split()
    N=int(line[0])
    Q=int(line[1])

    horses=[]
    for i in range(N):
        line=input().split()
        E=int(line[0])
        S=int(line[1])

        horses.append((E,S))

    directDistances=[]
    for i in range(N):
        line=input().split()
        directDistances.append([int(s) for s in line])

    shortestDists=[[directDistances[i][j] for j in range(N)] for i in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if (shortestDists[i][j]>shortestDists[i][k]+shortestDists[k][j] or
                    shortestDists[i][j]==-1) and \
                   shortestDists[i][k]!=-1 and shortestDists[k][j]!=-1:
                       shortestDists[i][j]=shortestDists[i][k]+shortestDists[k][j]


    ponyDists= [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if shortestDists[i][j] == -1:
                ponyDists[i][j] = -1
            elif shortestDists[i][j]<= horses[i][0]:
                ponyDists[i][j]= shortestDists[i][j]/horses[i][1]
            else:
                ponyDists[i][j]= -1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if (ponyDists[i][j]>ponyDists[i][k]+ponyDists[k][j] or
                    ponyDists[i][j]==-1) and \
                   ponyDists[i][k]!=-1 and ponyDists[k][j]!=-1:
                       ponyDists[i][j]=ponyDists[i][k]+ponyDists[k][j]

    print("Case #"+str(case+1)+":",end='')
    for i in range(Q):
        line=input().split()
        q1=int(line[0])-1
        q2=int(line[1])-1
        print(" "+str(ponyDists[q1][q2]),end='')
    print('')

