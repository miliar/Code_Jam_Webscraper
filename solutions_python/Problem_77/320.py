import sys

norDict = {0:0, 1:0, 2:1}
expDict = {0:0, 1:0, 2:2}
permDict = {0:1, 1:1}

def getperm(p):
    if p in permDict:
        a = permDict[p]
    else:
        a = p*getperm(p-1)
        permDict[p] = a
    #print('getperm',p,a)
    return a

def getcc(n,p):
    a = getperm(n)//(getperm(n-p)*getperm(p))
    #print('getcc',n,p,a)
    return a

def getnor(p):
    if p in norDict:
        return norDict[p]
    else:
        rs = getperm(p)
        #print('getperm',p,rs)
        rs -= 1 # all in position
        for i in range(1, p-1): # i number in position
            #print('>',p,i,getcc(p,i),getnor(p-i))
            rs -= getcc(p,i)*getnor(p-i)
        norDict[p] = rs
        return rs

def getexp(p):
    if p in expDict:
        return expDict[p]
    else:
        a = getperm(p)
        #print(a)
        rs = 1
        bc = 1
        for i in range(1,p-1):
            b = getcc(p,i)*getnor(p-i)
            #print('b=',b)
            bc += b
            rs += b*(1+getexp(p-i))
        #print('>',a-bc)
        rs += (a-bc)
        #print(rs)
        rs = rs/bc
        expDict[p] = rs
        return rs

def slove():
    icase = int(input())
    for i in range(icase):
        c = int(input())
        cs = [int(j) for j in input().split()]
        #print(cs)
        k = 0
        for j in range(len(cs)):
            if j+1 != cs[j]: k += 1
        #print('k=',k)
        print('Case #%d: %.6f'%(i+1,getexp(k)))

slove()


