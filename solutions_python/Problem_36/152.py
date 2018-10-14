fin=open('in.txt');
fout=open('out.txt','w');

S='welcome to code jam';
M=len(S);
T='';
L=0;
D={};

def f(i,j):
    if j==M:
        return 1;
    elif i==L:
        return 0;
        
    if (i,j) in D:
        return D[(i,j)];
    c=0;
    for n in range(i,L):
        if T[n]==S[j]:
            c+=f(n+1,j+1);
    D[(i,j)]=c;
    return c%10000;

for i in range(int(fin.readline())):
    T=fin.readline();
    L=len(T);
    D={};
    fout.write(str.format('Case #{}: {:04}\n',i+1,f(0,0)));
  
fout.close();
fin.close();
