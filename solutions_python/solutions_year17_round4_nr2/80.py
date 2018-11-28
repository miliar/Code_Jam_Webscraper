T=int(input())
for t in range (T):
    line=input().split()
    n=int(line[0])
    c=int(line[1])
    m=int(line[2])
    if c==2:
        persons=[[0 for i in range (n)]for j in range(2)]
        numtickets=[0,0]
        for i in range (m):
            line=input().split()
            p=int(line[0])
            b=int(line[1])
            persons[b-1][p-1]+=1
            numtickets[b-1]+=1
        if persons[0][0]+persons[1][0]<=max(numtickets[0],numtickets[1]):
            numrides=max(numtickets[0],numtickets[1])
            numuppg=0
            for i in range (n):
                numuppg+=max(0,persons[1][i]+persons[0][i] - numrides)
        else:
            numrides = persons[0][0]+persons[1][0]
            numuppg=0
        print ("Case #" + str(t+1) + ": " + str(numrides) + " " + str(numuppg))
