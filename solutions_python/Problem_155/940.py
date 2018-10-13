fout=open('Output2.out','w')
finp=open('A-large.in')
Input=finp.read().split()
T=int(Input[0])
for run in range(1,1+T):
    W=0
    Max=int(Input[(2*run) - 1])
    Str=[int(x) for x in Input[(2*run)]]
    c=0
    for i in range(0,Max+1):
        if Str[i]==0:
            if c<=i:
                W+=1
                c+=1
            else:
                continue
        else:
            c+=Str[i]
    fout.write("Case #%d: %d\n" %(run,W))
fout.close()
finp.close()
