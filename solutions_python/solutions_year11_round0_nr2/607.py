def reduce(combine,opposed,invoke):
    invoke_seq=list()
    for inv in invoke:
        invoke_seq.append(inv)
        if len(invoke_seq)<2:continue
        for com in combine:
            if com[0] in invoke_seq[-2:] and com[1] in invoke_seq[-2:]:
                if not (com[0]==com[1] and invoke_seq[-1]!=invoke_seq[-2]):
                    invoke_seq[-2:]=[com[2]]
                break
        for opp in opposed:
            if opp[0] in invoke_seq and opp[1] in invoke_seq:
                invoke_seq=list()
                break
    return invoke_seq

fin=open("in.txt")
fout=open("out.txt",mode="w")
i=0
for line in fin:
    if i:
        s=line.rstrip().split()
        c=int(s[0])
        d=int(s[c+1])
        n=int(s[c+d+2])
        print("Case #{}: [".format(i),end="",file=fout)
        ret=reduce(s[1:c+1],s[c+2:c+d+2],s[c+d+3])        
        for j in range(len(ret)):
            if j!=len(ret)-1:
                print(ret[j]+", ",end="",file=fout)
            else:
                print(ret[j],end="",file=fout)
        print("]",file=fout)
    i+=1