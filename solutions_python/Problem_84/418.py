import sys

for _ in range(int(sys.stdin.readline())):
    vv=list(map(int, sys.stdin.readline().strip().split(" ")))
    L=vv[0]
    C=vv[1]
    t=[['_' for j in range(C)]for i in range(L)]
    l=""
    b=False
    for i in range(L):
        l=sys.stdin.readline()
        for j in range(C):
            t[i][j]=l[j]
    for i in range(L):
        b=False
        for j in range(C):
            if t[i][j]=='#':
                if i+1<L and j+1<C and t[i][j+1]=='#' and t[i+1][j]=='#' and t[i+1][j+1]=='#':
                    t[i][j]='/'
                    t[i][j+1]='\\'
                    t[i+1][j]='\\'
                    t[i+1][j+1]='/'
                else:
                    print("Case #"+str(_+1)+": ")
                    print("Impossible")
                    b=True
                    break
        if b:
            break
    if b==False:
        print("Case #"+str(_+1)+": ")
        for i in range(L):
            R=""
            for j in range(C):
                R+=t[i][j]
            print(R)

      
        
        
