f=open("B-large.in")
out=open("output2.txt",'w')
def inp():
    for i in f:
        return i
def isPoss(h,n,m):
    for i in range(n):
        for j in range(m):
            if (anygreaterrow(h,i,j,n) and anygreatercol(h,i,j,m)):
                return False
    return True
def anygreaterrow(h,i,j,n):
    for p in range(n):
        if int(h[i][j])<int(h[p][j]):
            return True
    return False
def anygreatercol(h,i,j,m):
    for p in range(m):
        if int(h[i][j])<int(h[i][p]):
            return True
    return False
t=int(inp())
for i in range(t):
    h=[]
    n,m=[int(j) for j in inp().split()]
    for j in range(n):
        h.append(inp().split())
    if not(isPoss(h,n,m)):
        out.write("Case #"+str(i+1)+(": ")+" NO\n")
        #print "NO"
    else:
        out.write("Case #"+str(i+1)+(": ")+" YES\n")
        #print "YES"
        
f.close()
out.close()
