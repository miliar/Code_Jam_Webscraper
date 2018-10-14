
def flip(x,k,n):
    for i in range(k,k+n):
        if (x[i]==0):
            x[i]=1
        else:
            x[i]=0
    return x

def solve(x,n):
    newarr = []
    for i in x:
        if i=='+':
            newarr.append(1)
        else:
            newarr.append(0)
    #print(len(newarr))
    cnt = 0
    for i in range(0,len(newarr)-n+1):
        if newarr[i]==0:
            flip(newarr, i, n)
            #print(newarr)
            cnt+=1
        else:
            continue
    for i in newarr:
        if i==0:
            return "IMPOSSIBLE"
    return cnt

file = open("A-large.in","r")
cnt = 0
for line in file:
    if cnt==0:
        cnt+=1
    else:
        red = line.strip().split(" ")
        print("Case #"+str(cnt)+": " + str(solve(red[0],int(red[1]))))
        cnt+=1
