fin=open('A.in','r')
fout=open('A.out','w')
T=int(fin.readline())
for t in range(1,1+T):
    Sm,S=fin.readline().split()
    rf=0
    sta=0
    for si,sj in enumerate(S):
        if si>sta:
            k=si-sta
            rf+=k
            sta+=k
        sta+=int(sj)
    fout.write("Case #"+str(t)+": "+str(rf)+"\n")
fout.flush()
fin.close()
fout.close()
