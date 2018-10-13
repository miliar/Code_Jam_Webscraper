numberOfTestCase=input()
for z in range(numberOfTestCase):
    l=raw_input().strip("\n").split(" ")
    j=[]
    for i in range(int(l[0])+1):
        j.append(int(l[1][i]))
    k=0
    total=0
    extra=0
    for k in range(len(j)):
        total+=j[k]
        if len(j)-1!=k:
            if total<k+1:
                if j[k+1]>0:
                    p=(k+1)-total
                    extra+=p
                    total+=p
                    # print"EXTRA : Target: "+str(k+1)+" Total: "+str(total)+"What's next :"+str(j[k+1])+"Extra :"+str(extra)
    print"Case #"+str(z+1)+": "+str(extra)