t = int (input() )
for i in range(t):
    d,n = map(int,input().split() )
    horse=[]
    for j in range(n):
        temp1,temp2= map(int,input().split() )
        horse.append([temp1,temp2])

    ans=0
    for j in range(n):
        need = (d-horse[j][0])/horse[j][1]
        if(need > ans):
            ans=need
            
    print("Case #"+str(i+1)+": "+"{:.12f}".format(d/ans) )
        
