fin=open("A-large.in","r")
fout=open("A-large.out","w")
t=int(fin.readline())
for cas in xrange(1,t+1):
    arg=map(int,fin.readline().split())
    curr=arg[0]
    new=arg[1]
    built=[[""]]
    for i in xrange(curr):
        t1=fin.readline().split("/")
        if(t1[-1][-1]=="\n"):
            t1[-1]=t1[-1][:-1]
        built.append(t1)
        
        #print(built[-1])
    needed=0
    for j in xrange(new):
        t1=fin.readline().split("/")
        if(t1[-1][-1]=="\n"):
            t1[-1]=t1[-1][:-1]
        temp=t1
        maxi=-1
        maxloc=-1
        for i in xrange(len(built)):
            tmax=0
            for k in xrange(min(len(built[i]),len(temp))):
                if(built[i][k]!=temp[k]):
                    break
                tmax+=1
            if(tmax>maxi):
                maxi=tmax
                maxloc=i
        needed+=len(temp)-maxi
        for i in xrange(maxi,len(temp)):
            built.append(temp[:i+1])
            #print("mkdir ",built[-1])

    fout.write("Case #"+str(cas)+": "+str(needed)+"\n")
fout.close()
fin.close()
