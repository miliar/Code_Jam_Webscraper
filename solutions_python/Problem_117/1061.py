f = open("gjc32in.txt","r")

T = int(f.readline().strip())
def isPossible(i,j,lawn):
    square=lawn[i][j]
    hor=True
    ver=True
    for c in range(len(lawn[i])):
        if square<lawn[i][c]:
            hor=False
            break
    for r in range(len(lawn)):
        if square<lawn[r][j]:
            ver=False
            break
    return hor or ver

for case in range(1,T+1):
    print "Case #" + str(case)+":",
    N,M=map(int, f.readline().strip().split(" "))
    lawn=[]
    for e in range(N):
        lawn.append(map(int, f.readline().strip().split(" ")))

    possible=True
    for i in range(N):
        for j in range(M):
            if (not isPossible(i, j, lawn)):
                possible=False
                break
        if not possible:
            break
        
    if possible:
        print "YES"
    else:
        print "NO"        
    


    

