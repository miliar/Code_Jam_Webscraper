file=open("B-small-attempt0.in","r")

cases=int(file.readline()[:-1])
for z in range(cases):
    imp=(file.readline()[:-1]).split(" ")
    a=int(imp[0])
    b=int(imp[1])
    k=int(imp[2])

    alist=[]
    blist=[]
    klist=[]

    for i in range(0,a):
        alist.append(i)
    for j in range(0,b):
        blist.append(j)
    for l in range(0,k):
        klist.append(l)

    count=0

    if(len(alist)>len(blist)):
        for x in alist:
            for y in blist:
                if(x&y) in klist:
                    count+=1
    else:
        for x in blist:
            for y in alist:
                if(x&y) in klist:
                    count+=1
    print("Case #"+str(z+1)+": "+str(count))

    
        
