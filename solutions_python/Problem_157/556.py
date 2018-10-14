import copy

A=[[0,1,2,3,4,5,6,7],[1,4,3,6,5,0,7,2],[2,7,4,1,6,3,0,5],[3,2,5,4,7,6,1,0], \
   [4,5,6,7,0,1,2,3],[5,0,7,2,1,4,3,6],[6,3,0,5,2,7,4,1],[7,6,1,0,3,2,5,4]]
X=0
L=0
XL=0
s=[]
sv = 0

def fi():
    global A,L,s,XL
    Checked=[0,0,0,0,0,0,0,0]
    v = 0
    y = 0
    while Checked[v] < 1:
        Checked[v] = 1
        for i in range(0,L):
            v = A[v][s[i]]
            if v == 1:
                return y * L + i
        y = y + 1
    return -1

def f0(what,where):
    global A,L,s,XL
    w=where%L
    mm=where + 8*L
    if mm > XL:
        mm = XL
    v=s[w]
    if v == what:
        #print('f0a',what,w,where)
        return where
    for i in range(where+1,mm):
        w=i%L
        v=A[v][s[w]]
        if v == what:
            #print('f0b',what,w,i)
            return i
    return -1

def f1(what,where):
    global A,L,s,XL
    w=where%L
    v=what
    for i in range(where,XL):
        w=i%L
        v=A[v][s[w]]
        if v == what:
            return i
    return -1

def f2(where):
    global A,L,s,XL
    w=where%L
    v=0
    #print('f2',where)
    for i in range(where,XL):
        w=i%L
        #print('f2',i,w,v,s[w],A[v][s[w]])
        v=A[v][s[w]]
    #print("v =",v)
    return v

def f3(x):
    global A,sv
    if x == 0:
        return 0
    if x == 1:
        return sv
    x1 = int(x / 2)
    v1 = f3(x1)
    v2 = A[v1][v1]
    if (x % 2) == 1:
        v2 = A[v2][sv]
    return v2
    
T=int(input())
for t in range(0,T):
    Li = input().split(" ")
    L=int(Li[0])
    X=int(Li[1])
    XL = X * L
    S=input()
    s=[]
    #print(X,' * ',S)
    if (L * X) < 3:
        print("Case #%d: NO"%(t+1))
        continue
    if L == 1:
        print("Case #%d: NO"%(t+1))
        continue
    i1 = 0
    j1 = 0
    k1 = 0
    for i in range(0,L):
        if S[i] == 'i':
            s.append(1)
            i1 = 1
        elif S[i] == 'j':
            s.append(2)
            j1 = 0
        elif S[i] == 'k':
            s.append(3)
            k1 = 1
        else:
            error
    v = 0
    for i in range(0,L):
        v = A[v][s[i]]
    sv = v
    ans = ''
    v1 = f3(X)
    if v1 != 4:
        ans = 'NO'
    else:
        i = fi()
        if i < 0:
            ans = 'NO'
        else:
            j = f0(2,i+1)
            if j < 0:
                ans = 'NO'
            else:
                ans = 'YES'
    print("Case #%d: %s"%(t+1,ans))
    if (ans == 'YES') and (v1 != 4):
        print(S,"sv=%d X=%d v1=%d"%(sv,X,v1))
        error
