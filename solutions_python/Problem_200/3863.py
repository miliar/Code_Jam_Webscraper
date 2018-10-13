def tidylast(mm):
    for i in range(mm,0,-1):
        if tidy(i):
            return i
def tidy(n):
    d=list(str((n)))
    l=d[:]
    l.sort()
    if d==l:
        return(True)
    else:
        return(False)   
n=int(input())
inp=[]
out=[]
for i in range(0,n):
    inp.append(int(input()))
for i in range(0,n):
    out.append(tidylast(inp[i]))
for i in range(0,n):
    print('Case #',i+1,': ',out[i],sep='')
