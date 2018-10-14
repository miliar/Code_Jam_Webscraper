def impossible(i,j,n,m,lawn):
    p=0
    for x in range(n):
        if lawn[i][j]<lawn[x][j]:
            p+=1
            break
    for x in range(m):
        if lawn[i][j]<lawn[i][x]:
            p+=1
            break
    if p==2:
        return True
    else:
        return False

def solve(n,m,lawn):
    for i in range(n):
        for j in range(m):
            if impossible(i,j,n,m,lawn):
                return "NO"
                break
    return "YES"

fi = open("B-small-attempt0.in","r")
fo = open("B-small-attempt0.out","w")

t = int(fi.readline())

for i in range(1,t+1):
    lawn=[]
    fl=fi.readline()
    d=fl.split()
    n=int(d[0])
    m=int(d[1])
    for j in range(n):
        lawn.append(fi.readline().split())
    o= "Case #"+str(i)+": "+solve(n,m,lawn)
    print o
    fo.write(o+"\n")

fo.close()
fi.close()
print "Done!"
