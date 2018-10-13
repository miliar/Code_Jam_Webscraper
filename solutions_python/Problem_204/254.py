import math
filename ="B-small-attempt1.in"
f= open(filename,'r')
out = open("output.txt",'w')
Cases= int(f.readline())
for T in range(Cases):
    [N,P]=[int(j) for j in f.readline().split(" ")]
    R=[int(j) for j in f.readline().split(" ")]
    Q=[[int(j) for j in f.readline().split(" ")] for i in range(N)]
    for i in range(len(Q)):
        Q[i].sort()
    #print(Q)
    for i in range(len(Q)):
        Q[i] = [[math.ceil(j/(1.1*R[i])),int(j/(0.9*R[i]))] for j in Q[i]]
        Q[i] = [j for j in Q[i] if j[0]<=j[1]]
    print(Q)
    packs =0
    while True:
        br =False
        for i in range(len(Q)):
            if len(Q[i])==0:
                br=True
        if br:
            break
        L = max([Q[i][0][0] for i in range(len(Q))])
        R = min([Q[i][0][1] for i in range(len(Q))])
        if L<=R:
            packs +=1
            Q=[i[1:] for i in Q]
        else:
            I = [i for i in range(len(Q)) if Q[i][0][1]==R]
            for i in I:
                Q[i]=Q[i][1:]
    ret=str(packs)
    ret="Case #"+str(T+1)+": "+ret
    print(ret)
    out.write(ret+"\n")
f.close()
out.close()
