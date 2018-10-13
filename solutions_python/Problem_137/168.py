import sys


with open('C-large.in','r') as f:
	data=f.readlines()

N=int(data[0]);
res="";


for i in range(N):
    [R,C,M]=[int(_) for _ in data[1+i].split()]
    s=""
    n_vide=R*C-M
    if min(R,C)==1:
        for r in range(R):
            for j in range(C):
                if max(r,j)+1==1: s+="c"
                elif max(r,j)+1<=n_vide: s+="."
                else: s+="*"
            s+="\n"
    elif min(R,C)==2:
        if n_vide==1 or (not n_vide%2 and n_vide>=4):
            for r in range(R):
                for j in range(C):
                    if max(r,j)+1==1: s+="c"
                    elif max(r,j)+1<=n_vide/2: s+="."
                    else: s+="*"
                s+="\n"
        else: s+="Impossible\n"
    else:
        if n_vide in [2,3,5,7]:
            s+="Impossible\n"
        elif n_vide==1 or (n_vide>=2*(C+R)-4) or (not n_vide%2):
            for r in range(R):
                for j in range(C):
                    if max(r,j)+1==1: s+="c"
                    elif (r<=1) and (j<n_vide/2): s+="."
                    elif (j<=1) and (r<2+(n_vide/2-C)): s+="."
                    elif j-2+(r-2)*(C-2)<n_vide-(2*(C+R)-4): s+="."
                    else: s+="*"
                s+="\n"
        else:
            for r in range(R):
                for j in range(C):
                    if max(r,j)+1==1: s+="c"
                    elif (r<=2) and (j<=2): s+="."
                    elif (r<=1) and (j<(n_vide-1)/2-1): s+="."
                    elif (j<=1) and (r<2+(n_vide-1)/2-C): s+="."
                    else: s+="*"
                s+="\n"
    res+="Case #"+str(i+1)+": \n"+s

#print res

with open('res.txt', 'w') as f:
	f.write(res)
