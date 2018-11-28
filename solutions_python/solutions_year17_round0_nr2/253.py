def makeTidy(n):
    if int(n)<10:
        return n
    l=len(n)
    ctr=0
    for i in range(l-1):
        if n[i]>n[i+1]:
            z=int(n[i])-1
            #print z,i,n[i]
            n=n[0:i-ctr]+str(z)+'9'*(l-i-1+ctr)
            break
        elif(n[i]==n[i+1]):
            ctr+=1
        else:
            ctr=0
    return n


for t in range(input()):
    n=raw_input()
    n=makeTidy(n)
    n=int(n)

    print "Case #"+str(t+1)+": "+str(n)

    
