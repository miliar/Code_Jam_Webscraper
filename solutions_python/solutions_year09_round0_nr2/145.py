MAX=10000;

def sink(T,B,i,j):
    P=[(i,j)];
    i+=1;
    j+=1;
    while True:
        if B[i-1][j-1]!='':
            return P,B[i-1][j-1];
        m=min(T[i][j],T[i-1][j],T[i+1][j],T[i][j-1],T[i][j+1]);
        if T[i][j]==m:
            return P,'';
        else:
            if T[i-1][j]==m:
                i-=1;
            elif T[i][j-1]==m:
                j-=1;
            elif T[i][j+1]==m:
                j+=1;
            elif T[i+1][j]==m:
                i+=1;
            P.append((i-1,j-1));

fin=open('in.txt');
fout=open('out.txt','w');

for n in range(int(fin.readline())):
    (H,W)=(int(t) for t in fin.readline().split());
    T=[[MAX]*(W+2)];
    for i in range(H):
        T.append([MAX]+[int(t) for t in fin.readline().split()]+[MAX]);
    T.append([MAX]*(W+2));

    B=[['' for i in range(W)] for j in range(H)];
    s0='a';
    for i in range(H):
        for j in range(W):
            [P,s]=sink(T,B,i,j);
            if s=='':
                s=chr(ord(s0));
                s0=chr(ord(s0)+1);
            for p in P:
                B[p[0]][p[1]]=s;

    fout.write(str.format('Case #{}:\n',n+1));
    for l in B:
        fout.write(' '.join(l)+'\n');

fout.close();
fin.close();
    
