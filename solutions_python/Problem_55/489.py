fin=open("C-small-attempt0.in","r")
fout=open("roller_small.out","w")

T=int(fin.readline().strip())

for i in range(T):
    params = fin.readline().strip().split()
    R=int(params[0])
    K=int(params[1])
    N=int(params[2])

    groups = fin.readline().strip().split()

    gcount=0
    for j in range(R):
        count = 0
        x=0
        #print len(groups)
        while True:
            temp = count + int(groups[0])
            #print groups
            if temp <= K and x<len(groups):
                count = temp
                groups.append(groups.pop(0))
                #print groups
            else:
                #print "count = " + str(count)
                gcount += count
                #print "gcount = " +str(gcount)
                break
            x += 1

    #print str(gcount)
    if (i==(T-1)):
        fout.write("Case #" +str(i+1)+ ": " + str(gcount))
    else:
        fout.write("Case #" +str(i+1)+ ": " + str(gcount) + "\n")

fout.close()
fin.close()
    

