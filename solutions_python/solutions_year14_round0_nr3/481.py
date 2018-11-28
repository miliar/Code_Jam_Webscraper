T=int(input())

M = [[0 for col in range(12)] for row in range(12)]

def Test(x,y):
    global M
    global Empty
#    print(x,y)
    cnt=0
    P=[[0 for col in range(8)] for row in range(8)]
    if M[x-1][y]=="*":
        P[cnt][0]=x-1
        P[cnt][1]=y
        cnt=cnt+1
    if M[x-1][y-1]=="*":
        P[cnt][0]=x-1
        P[cnt][1]=y-1
        cnt=cnt+1
    if M[x-1][y+1]=="*":
        P[cnt][0]=x-1
        P[cnt][1]=y+1
        cnt=cnt+1
    if M[x+1][y]=="*":
        P[cnt][0]=x+1
        P[cnt][1]=y
        cnt=cnt+1
    if M[x+1][y-1]=="*":
        P[cnt][0]=x+1
        P[cnt][1]=y-1
        cnt=cnt+1
    if M[x+1][y+1]=="*":
        P[cnt][0]=x+1
        P[cnt][1]=y+1
        cnt=cnt+1
    if M[x][y-1]=="*":
        P[cnt][0]=x
        P[cnt][1]=y-1
        cnt=cnt+1
    if M[x][y+1]=="*":
        P[cnt][0]=x
        P[cnt][1]=y+1
        cnt=cnt+1
    if cnt>Empty:
        return 0
    if cnt==Empty:
#        print("P=",P)
#        print("M=",M)
        M[x][y]="."
        for k in range(0,cnt):
            M[P[k][0]][P[k][1]]="."
        return 1
    if cnt==0:
        return 0
    sav=M[x][y]
    M[x][y]="."
    Empty-=cnt
    for k in range(0,cnt):
        M[P[k][0]][P[k][1]]="."
    for k in range(0,cnt):
        if Test(P[k][0],P[k][1])>0:
            return 1
    M[x][y]=sav
    for k in range(0,cnt):
        M[P[k][0]][P[k][1]]="*"
    Empty+=cnt
    return 0

def Test1(x,y):
    global M
    global Empty
    Empty-=1
    M[x][y]="c"
    testok=Test(x,y)
    if testok==0:
        M[x][y]="*"
    else:
        M[x][y]="c"
    Empty+=1
    return testok


for t in range(0,T):
    L=input().split()
    R=int(L[0])
    C=int(L[1])
    N=int(L[2])
    Points=R*C
    Empty=Points-N
#    print("--------",R,C,Points,Empty)
    for i in range(0,C+2):
        M[0][i]="E"
        M[R+1][i]="E"
    for j in range(1,R+1):
        M[j][0]="E"
        M[j][C+1]="E"
        for i in range(1,C+1):
            M[j][i]="*"
    for k in range(1,C+1):
        s=""
        for l in range(1,R+1):
            s+=M[l][k]
#        print(s)
    print("Case #%d:"%(t+1))
    if R==1:
        if N<C:
            s=""
            for i in range(0,N):
                s+="*"
            for i in range(N,Points-1):
                s+="."
            s+="c"
            print(s)
        else:
            print("Impossible")
    elif C==1:
        if N<R:
            for i in range(0,N):
                print("*")
            for i in range(N,Points-1):
                print(".")
            print("c")
        else:
            print("Impossible")
    elif Empty==1:
        s="c"
        for i in range(1,C):
            s=s+"*"
        print(s)
        s=""
        for i in range(0,C):
            s=s+"*"
        for i in range(1,R):
            print(s)
    else:
        testok=Test1(1,1)
        if testok==0:
            if R>1:
                testok=Test1(2,1)
                if testok==0:
                    if C>1:
                        testok=Test1(2,2)
            elif C>1:
                if testok==0:
                    testok=Test1(1,2)
        if testok==1:
            for r in range(1,R+1):
                s=""
                for c in range(1,C+1):
                    s+=M[r][c]
                print(s)
        else:
            print("Impossible")
