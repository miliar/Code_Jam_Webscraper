import sys

def get_score(war_n,war_k):
    s=0
    while len(war_n):
        if war_n[0]>war_k[0]:
            s+=1
            war_n.pop(0)
            war_k.pop(0)
        else:
            war_n.pop(0)
            war_k.pop()
    return s

with open('D-large.in','r') as f:
	data=f.readlines()

N=int(data[0]);
res="";


for i in range(N):
    n0=int(data[i*3+1])
    B_n=[float(_) for _ in data[i*3+2].split()]
    B_k=[float(_) for _ in data[i*3+3].split()]

    B_n.sort()
    B_k.sort()

    y=get_score(B_n[:],B_k[:])
    z=n0-get_score(B_k[:],B_n[:])

    res+="Case #"+str(i+1)+": "+str(y)+" "+str(z)+"\n"

#print res

with open('res.txt', 'w') as f:
	f.write(res)
