myfile=open("A-large.in", "r")
inp=myfile.read().split("\n")

fullanswer=""
i=0
for casenumber in range(int(inp[0])):
    i+=1
    val=inp[i].split(" ")

    x=1
    pO=1
    pB=1
    time=0
    curr=val[x]
    timeusedbyprev=0

    for k in range(int(val[0])):
        if val[x]=="O":
            x+=1
            nO=int(val[x])
            amountofsec=nO-pO

            pO=nO
            if amountofsec<0: amountofsec*=-1            

            if curr=="O":
                amountofsec+=1
                time+=amountofsec
                timeusedbyprev+=amountofsec
                
            else:
                
                curr="O"
                amountofsec-=timeusedbyprev
                if amountofsec<0: amountofsec=0
                amountofsec+=1
                time+=amountofsec
                timeusedbyprev=amountofsec
                
        elif val[x]=="B":
            x+=1
            nB=int(val[x])

            amountofsec=nB-pB
         
            pB=nB

            if amountofsec<0: amountofsec*=-1

            if curr=="B":
                amountofsec+=1
                time+=amountofsec
                timeusedbyprev+=amountofsec              
            else:
                curr="B"
                amountofsec-=timeusedbyprev
                if amountofsec<0: amountofsec=0
                amountofsec+=1
                time+=amountofsec
                timeusedbyprev=amountofsec
        x+=1

    fullanswer+="Case #%d: %d\n" % (casenumber+1,time)
print fullanswer

results=open("A.out","w")
results.write(fullanswer)
myfile.close()
results.close()
