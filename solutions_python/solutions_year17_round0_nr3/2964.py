from math import ceil as c
t = int(input())

def getindexleft(a, i):
    
    i -= 1
    while(i!=0):
        if(a[i] == 1):
            break
        i -= 1
    return i
    
def getindexright(a,i):
    
    i+=1
    while(i!=n+1):
        if(a[i] == 1):
            break
        i += 1
    return i

def maximum_diff(l):

    count = 0
    i = 1
    d = []
    e = []
    while(i < n+2):
        j = i
        count = 0
        while(j < n+2):
            if(l[j] != 1):
                count += 1
            elif(l[j] == 1):
                break
            j += 1
        d.append(count)
        e.append(j - count)
        i = j + 1
    return e,d

for m in range(t):
    n,k = input().split()
    n = int(n)
    k = int(k)
    
    a = []
    for i in range(n+2): 
        if(i==0 or i==n+1):
            a.append(1)
        else:
            a.append(0)
    
    for i in range(k - 1):
        p,q = maximum_diff(a) 
        h = p[q.index(max(q))]
        a[h + c(max(q)/2) - 1] = 1
        v = h + c(max(q)/2) - 1
    
    p,q = maximum_diff(a)
    h = p[q.index(max(q))]
    a[h + c(max(q)/2) - 1] = 1
    s = h + c(max(q)/2) - 1
    ls = (s - getindexleft(a,s) - 1)
    rs = (getindexright(a,s) - s - 1)
    print("Case #%d: %d %d" %(m+1, max(ls,rs), min(ls,rs)))