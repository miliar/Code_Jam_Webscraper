from itertools import count
import math


def getAllMaxFuncs(f,xs):
    maxx = max(xs,key = f)
    value = f(maxx)
    return [x for x in xs if f(x)== value]
def mindiff(x):
    return min(x[1],x[2])

def maxdiff(x):
    #print("maxd",x)
    return max(x[1],x[2])


def rekresult(n,k):             
    if n%2==1:
        return (int(n/2),int(k/2))
    if n%2==0:
        return (int(n/2)-(k%2),int(k/2))


def result(n,k):
    if n >10 and k > 10:
        rek = rekresult(n,k)
        return result(*rek)
    used = [-1,n]
    for p in range(k):
        #print(used)
        
        zipped = zip(used, used[1:])
        zipped2 = zip(used, used[1:])
        diffs = [(b-a,a,b) for a,b in zipped]+[(b-a+1,a,b) for a,b in zipped2 if (b-a) % 2 == 1]
       
        #print(diffs)
        diffs2 = [(int(d/2)+a,a,b) for d,a,b in diffs]
        diffs3 = [(d,d-a,b-d,a,b) for d,a,b in diffs2] 
        #print("diffs:",diffs3)
        y = getAllMaxFuncs(mindiff,diffs3)
        z = getAllMaxFuncs(maxdiff,y)

        (stall,ls,rs,a,b) = z[0]
        used.append(stall)
        used = sorted(used)
        #print("#"*30)
        if p == k-1:
            #print(used)
            return (max(ls,rs)-1,min(ls,rs)-1)
t = int(input()) 
for i in range(1, t + 1):    
    n,k = [int(k) for k in input().split(" ")]
    if n<0: break
    r1 = result(n,k)
    print("Case #{}: {} {}".format(i, *r1))

    
    
    
    