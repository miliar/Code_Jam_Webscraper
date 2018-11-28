import sys

def dps(C,F,X):
    f0=0
    f0=2;
    if X<=C: return str(X/f0)
    t=0;
    t0=0;
    t+=C/f0;
    while f0<=(X/C-1)*F:
        f0+=F
        t+=C/f0    
    t+=(X-C)/f0
    return str(t)

with open('a.in','r') as f:
	data=f.readlines()

N=int(data[0]);
res="";


for i in range(N):
    [C,F,X]=[float(_) for _ in data[1+i].split()]
    res+="Case #"+str(i+1)+": "+dps(C,F,X)+"\n"

with open('b.txt', 'w') as f:
	f.write(res)
