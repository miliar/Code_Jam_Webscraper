f = open('output', 'w')
def fm(a,b):
    if len(a)==2:
        if len(b)==2:
            return m(a[1],b[1])
        else:
            return '-'+fm(a[1],b)
    if a=='1':
        return b
    if b=='1':
        return a
    if a==b:
        return '-1'
    if a=='i':
        if b=='j':
            return 'k'
        elif b=='k':
            return '-j'
    if a=='j':
        if b=='i':
            return '-k'
        elif b=='k':
            return 'i'
    if a=='k':
        if b=='i':
            return 'j'
        elif b=='j':
            return '-i'
def m(a,b):
    c=fm(a,b)
    if len(c)>2:
        while c[0]=='-' and c[1]=='-':
            c=c[2:]
    return c
    
T=input()
a=[]
for i in range(T):
    L,X=[int(n) for n in raw_input().split()]
    l=raw_input()
    S=l*X
    k,j=S[0],1
    while k!='i' and j!=len(S):
        k=m(k,S[j])
        j+=1
    S=S[j:]
    if S=='':
        a.append('NO')
        continue
    k,j=S[0],1
    while k!='j' and j!=len(S):
        k=m(k,S[j])
        j+=1
    S=S[j:]
    if S=='':
        a.append('NO')
        continue
    k,j=S[0],1
    while j!=len(S):
        k=m(k,S[j])
        j+=1
    if k=='k':
        a.append('YES')
    else:
        a.append('NO')
for i in range(T):
    f.write('Case #'+str(i+1)+": "+a[i]+"\n")
