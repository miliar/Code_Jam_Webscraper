def ispal(N):
    s=str(N);
    S=s[::-1];
    return long(S)==long(s)
def main():
    import math as m
    f=open('C-small-attempt6.in','r');
    F=[];
    for line in f:
        F.append(line);
    k=int(F[0]);
    S=[];
    for i in range(1,len(F)):
        s=F[i];
        L=s.find(' ');
        a=long(s[:L]);
        b=long(s[L+1:]);
        A=long(m.ceil(m.sqrt(a)));
        B=long(m.ceil(m.sqrt(b)));
        if (A-1)**2>=a:
            A-=1;
        if B**2<=b:
            B+=1;
        S.append(range(A,B));
    R='';
    for i in range(k):
        ctr=0;
        for j in range(len(S[i])):
            ctr+=int(ispal(S[i][j]) and ispal(S[i][j]**2));
        R+='Case #'+str(i+1)+': '+str(ctr)+'\n';
    open('P2.txt','w').write(R);
