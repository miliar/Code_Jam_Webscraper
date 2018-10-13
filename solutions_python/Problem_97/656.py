f=open("C-large.in.txt")
o=open("output.txt","w")
t=int(f.readline())
line=f.readline()
case=1
while line:
    outline="Case #%d: "%case
    line=line.split()
    a=int(line[0])
    b=int(line[1])
    count=0
    for n in range(a,b):
        N=str(n)
        myTuple=tuple()
        for s in range(1,len(N)):
            M=N[s:]+N[:s]
            m=int(M)
            if m>n and m<=b:
                if m not in myTuple:
                    myTuple+=(m,)
                    count+=1
    outline+=str(count)
    o.write(outline)
    o.write('\n')
    case+=1
    line=f.readline()
f.close()
o.close()
