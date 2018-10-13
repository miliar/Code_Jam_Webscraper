ct=0
def mp(sss,k):
    for i in range(0,len(sss)):
        if sss[i]=='-' and i<=len(sss)-k:
            return i
        elif i>len(sss)-k and sss[i]=='-':
            return i-k+1
def stri(s):
    s1=''
    for i in range(0,len(s)):
        s1+=s[i]    
    return s1
def cp(s):
    c=0
    for i in range(0,len(s)):
       if s[i]=='+':
           c+=1
       else:
           break
    return c
def flip(s,c,st):
    s=list(s)
    global ct
    ct+=1
    for i in range(st,st+c):
        if s[i]=='+':
            s[i]='-'
        elif s[i]=='-':
            s[i]='+'    
    return(stri(s))    
f=''
im=[]
out=[]
k=[]
n=int(input())
for i in range(0,n):
    s=input().strip().split(' ')
    im.append(s[0])
    k.append(int(s[1]))    
for i in range(0,n):
    ct=0
    while (cp(im[i])!=len(im[i])):
        if ct<2000:
           im[i]=flip(c=k[i],s=im[i],st=mp(im[i],k[i]))
        else:
            out.append('IMPOSSIBLE')
            break
    else:
        out.append(ct)
for i in range(len(out)):
    print('Case #',i+1,': ',out[i],sep='')
    
