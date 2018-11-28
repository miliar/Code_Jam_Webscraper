import sys

x = 0;
n = sys.stdin.readline()
n = int(n)

while (x < n):
    x = x + 1 #count
    
    xy = sys.stdin.readline().split()
    
    lis = []
    
    for i in range(int(xy[0])):
        lis.append(sys.stdin.readline().split())
        
    noflag = 0
    for i in range(int(xy[0])):
        for j in range(int(xy[1])):
            nox = noy = 0;
            for k in range(int(xy[1])):
                if lis[i][j] < lis[i][k]:
                    nox = 1
            for k in range(int(xy[0])):
                if lis[i][j] < lis[k][j]:
                    noy = 1
            if nox == 1 and noy == 1:
                noflag = 1
    
    if noflag == 0:
        print("Case #",x,": YES", sep='')
    else:
        print("Case #",x,": NO", sep='')