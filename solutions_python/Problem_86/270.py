def Har(x,y):
    return (x%y==0 or y%x==0)

def ToInt(X):
    R=[]
    i=0
    while i<len(X):
        R.append(int(X[i]))
        i=i+1
    return R

def HarX(X,n):
    res=True
    i=0
    while i<len(X):
        if(not(Har(X[i],n))):
           res=False
           break
        i=i+1
    return res

def InHar(Notes,Others):
    Min = int(Notes[1])
    Max = int(Notes[2])
    i = Min
    O=ToInt(Others)
    while i<Max+1:
        if(HarX(O,i)):
            return str(i)
            break
        i=i+1
    return "NO"

f = open("test.in")
out = open("test.out","w")
lines = 0
N = int(f.readline())
for i in range(N):
    if lines!=0:
        out.write("\n")
    lines=1
    Notes = f.readline().split()
    Others = f.readline().split()
    out.write("Case #"+str(i+1)+": "+str(InHar(Notes,Others)))
out.close()
f.close()


