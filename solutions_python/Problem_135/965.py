def match(l1,l2):
    l=[]
    for i in l1:
       if i in l2:l.append(i)
    return(l)

T=int(input())
for i in range(1,T+1):
        (grid1,grid2)=([],[])
        r1=int(input())
        for k in 1,2,3,4:
            tmp=input().split()
            map(int,tmp)
            grid1.append(tmp)
        r2=int(input())
        for k1 in 1,2,3,4:
            tmp=input().split()
            map(int,tmp)
            grid2.append(tmp)
        l=match(grid1[r1-1],grid2[r2-1])
        if len(l)==0:print("Case #",i,": ","Volunteer cheated!",sep='')
        if len(l)==1:print("Case #",i,": ",l[0],sep='')
        if len(l)>1 :      print("Case #",i,": ","Bad magician!",sep='')

