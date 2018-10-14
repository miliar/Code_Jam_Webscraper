def decide(X):
    Out=['NO','YES'];
    m=len(X);
    n=len(X[0]);
    C=[[0 for i in range(m)] for j in range(n)]
    D=0;
    check=1;
    print len(C),len(C[0]),C
    for i in range(m):
        for j in range(n):
            C[j][i]=X[i][j];
    i=0;
    while check==1 and i<m:
        j=0;
        while check==1 and j<n:
            x=X[i][j];
            k=(x==min(X[i]) and X[i].count(x)==n) or (x==min(C[j]) and C[j].count(x)==m) or x>min(X[i]) or x>min(C[j]);
            j+=1
            check*=int(k);
        i+=1;
    if check==1:
        D=1;
    return Out[D]
def main():
    f=open('B-small-attempt0.in','r');
    F=[];
    for line in f:
        F.append(line);
    T=long(F[0]);
    i=1;
    Data=[];
    V=[];
    while i<len(F):
        x=F[i];
        k=x.find(' ');
        N=long(F[i][:k]);
        M=long(F[i][k+1:]);
        Data.append(F[(i+1):(i+N+1)]);
        i+=1+N;
        V.append([N,M]);
    for i in range(T):
        for j in range(V[i][0]):
            s=Data[i][j];
            L=[];
            k=s.find(' ');
            L.append(long(s[:k]));
            ctr=1;
            while ctr<V[i][1]:
                ctr+=1;
                k_new=s.find(' ',k+1);
                L.append(long(s[(k+1):k_new]));
                k=k_new;
            Data[i][j]=L;
    R='';
    for i in range(len(Data)):
        print i,Data[i]
        R+='Case #'+str(i+1)+': '+decide(Data[i])+'\n';
    open('P3.txt','w').write(R);
