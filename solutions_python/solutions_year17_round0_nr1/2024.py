andmed=open("pin.txt", "r")
t=int(andmed.readline())
outs=list()
for i in range(t):
    mitu=0
    tempr=andmed.readline().split()
    k=int(tempr[1])
    seq=list(tempr[0])
    n=len(seq)
    for j in range(n):
        if seq[j]=="-":
            if j+k>n:
                mitu="IMPOSSIBLE"
                break
            else:
                mitu+=1
                for x in range(j, j+k):
                    if seq[x]=="-":
                        seq[x]="+"
                    else:
                        seq[x]="-"
    vastus="Case #"+str(i+1)+": "+str(mitu)
    outs.append(vastus)
andmed.close()


outgo=open("pout.txt","w")
for asi in outs:
    outgo.write(asi)
    outgo.write("\n")
outgo.close()
