f = open("input10.in", "r")
fout = open("output4b.out", "w")
tot = f.readlines()

T = int(tot[0]) # numero di casi

indexstart = 1
indexstop = 4
i = 0
e = 0.0000001
for x in range(T):
    i+=1
    shit = tot[indexstart:indexstop]
    indexstart=indexstop
    indexstop=indexstop+3
    #print shit

    N = int(shit[0])
    firstlist= []
    secondlist = []
    
    naomi=[]
    ken=[]
    
    firstlist = (shit[1].strip().split(" ")) # e ora ho la lista 
    secondlist = shit[2].strip().split(" ") # e ora ho la lista

    #print firstlist
    #print secondlist
    for y in firstlist:
        naomi.append(float(y))
    for y in secondlist:
        ken.append(float(y))

    naomi.sort()
    ken.sort()
    
    naomi2=naomi[:]
    naomi2.reverse()
    ken2=ken[:]
    ken2.reverse()
    
    j=0
    #print naomi
    result=0
    #print naomi
    #print ken

    y=0
    while(1):
        if(len(naomi)==0):
            break
        if(naomi[0]<ken[0]):
            y+=1
            ken.pop()
            naomi.pop(0)
        else:
            ken.pop(0)
            naomi.pop(0)
            result+=1
    #print naomi
    #print ken
    #result=len(naomi)










    
    y=0
    result2=0
    #print "=="
    #print naomi2
    #print ken2
    while(1):
        if(len(ken2)==0):
            break
        if(ken2[y]<naomi2[y]):
            ken2.pop()
            naomi2.pop(0)
            result2+=1
        else:
            ken2.pop(0)
            naomi2.pop(0)



    
        #if(y>ken[j]):
        #    result = N-j
        #    print j
        #    break
        #j+=1

    #print (result), result2
    fout.write("Case #{0}: {1} {2}\n".format( i, (result), result2))
    #print "----"
f.close()
fout.close()

























    
