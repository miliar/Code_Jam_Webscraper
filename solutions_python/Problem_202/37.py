# x is a rook
# + is a bishop
# o is a queen

# x and + can't attack each other
# so rooks and bishops are independent, do them separately

import sys
sys.stdin=open("data.txt")
sys.stdout=open("out.txt","w")
input=sys.stdin.readline

t=int(input())

for cnum in range(t):
    n,m=map(int,input().split())
    # get rook and bishop order
    o1=[]   # rook
    o2=[]   # bishop
    for i in range(n):
        for j in range(n):
            o1.append((i,j))
    for i in range(n-1):        # keep i+j constant
        for j in range(i+1):
            # cell is (j,i-j)
            # other cell is (n+1-j,n+1-i+j)
            o2.append((j,i-j))
            o2.append((n-1-j,n-1-i+j))
    for j in range(n):
        o2.append((j,n-1-j))
    #print(o1,o2)
    #continue
    tx1=set()
    ty1=set()
    tx2=set()
    ty2=set()
    # get models
    g1=[[0]*n for _ in range(n)]
    g2=[[0]*n for _ in range(n)]
    p1=[]
    p2=[]
    for _ in range(m):
        p,x,y=input().split()
        if p in 'ox':   # rook
            g1[int(x)-1][int(y)-1]+=1
            g2[int(x)-1][int(y)-1]+=1
            tx1.add(int(x)-1)
            ty1.add(int(y)-1)
        if p in 'o+':   # bishop
            g1[int(x)-1][int(y)-1]+=2
            g2[int(x)-1][int(y)-1]+=2
            tx2.add(int(x)+int(y)-2)
            ty2.add(int(x)-int(y))
    # put in extra stuff
    for x,y in o1:  # rook
        if (x not in tx1) and (y not in ty1):
            tx1.add(x)
            ty1.add(y)
            g2[x][y]+=1
    for x,y in o2:  # bishop
        if (x+y not in tx2) and (x-y not in ty2):
            tx2.add(x+y)
            ty2.add(x-y)
            g2[x][y]+=2
    # get answer
    output=[]
    ans=0
    for i in range(n):
        for j in range(n):
            ans+=[0,1,1,2][g2[i][j]]
            if g1[i][j]!=g2[i][j]:
                output.append("%s %d %d"%(".x+o"[g2[i][j]],i+1,j+1))
    print("Case #%d: %d %d"%(cnum+1,ans,len(output)))
    for l in output: print(l)