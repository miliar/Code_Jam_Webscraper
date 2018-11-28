f = open("A-large.in")
g = open(f.name[:-3]+".out", 'w')
T = f.readline().strip()
T = int(T)
#T=1

for t in range(T):   
    numstring = f.readline().strip()
    #numstring='111111110'             
    numlist = map(lambda (x):x, numstring)
    numdict = dict([(x, -1) for x in numlist])
    numdict[numlist[0]] = 1
    for d in numlist[1:]:
        if numdict[d]==-1:
            numdict[d]=0
            break
    i=2
    for d in numlist:
        if numdict[d]==-1:
            numdict[d]=i
            i=i+1
    num=0
    b=len(numdict)
    if b==1:
        b=2
    j = len(numlist)-1
    for d in numlist:
        num = num + (b**j)*numdict[d]
        j=j-1

    stringy = "Case #"+str(t+1)+": "+str(num)
    print stringy
    g.write(stringy+"\n")

f.close()
g.close()


        
    
