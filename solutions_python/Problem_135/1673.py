import math
def solve(grid1,grid2,first,second):
    possible=grid1[first-1]
    otherPossible=grid2[second-1]
    x=-1
    for each in possible:
        if each in otherPossible:
            if not x==-1:
                return "Bad magician!"
            x=each
    if x==-1:
        return "Volunteer cheated!"
    return x
    

X=open("a2.in")
z=open("output.txt","w")
case=0
cases=int(X.readline())
line=X.readline()
while case<cases:
    case+=1
    print case
    first=int(line)
    grid1=[]
    grid2=[]
    for index in range(0,4):
        grid1.append(X.readline().split())
    line=X.readline()
    second=int(line)
    for index in range(0,4):
        grid2.append(X.readline().split())
    z.write("Case #"+str(case)+": "+solve(grid1,grid2,first,second)+"\n")
    line=X.readline()
z.close()
