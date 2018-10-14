f= open("1in.txt").read().split("\n")
writeF=open("1out.txt","w")




times=1
end=10
i=1
while(True):
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!%d"%i)
    DandN=f[i].split(" ")
    D=int(DandN[0]);
    N=int(DandN[1]);
    # print("D:%d N:%d"%(D,N))

    current=0
    time=0
    end+=N
    for j in range(int(i)+1,N+int(i)+1):
        kands=f[j].split(" ")
        K=int(kands[0])
        S=int(kands[1])
        # print("%d %d"%(K,S))
        # print("time is %lf " %((D-K)/S))
        if(time<=(D-K)/S):
            time=(D-K)/S
        # temp=current
        current=round(D/time,7)
        # print("current: %lf,D:%d:,D/current: %lf"%(current,D,D/current))
    
    print("Case #%d: %lf \n" %(times,current))

    writeF.write("Case #%d: %lf \n" %(times,current))
    times+=1
    i+=N+1
    
f.close()
writeF.close()