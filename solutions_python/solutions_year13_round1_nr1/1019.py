fout=open("bullseye-small-out.txt", "wb+")
f = open("bulley.in", "r+")


#i = raw_input()
i=f.readline()

T=int(i)
temp=T
while T>0:
    #i=raw_input()
    i=f.readline()
    r=long(i.split(" ")[0])
    k=long(i.split(" ")[1])
    Case=True
    N=1
    while Case:
        computed=(2*N*N)+(((2*r)-1)*N)
        if computed>k:
            #print "case #"+str(temp-T+1)+": "+str(N-1)
            fout.write("Case #"+str(temp-T+1)+": "+str(N-1))
            fout.write("\n")
            Case=False
        N=N+1
    T=T-1
fout.close()
f.close()
print "over"
