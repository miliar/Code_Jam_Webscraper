#Reading and opening file in data
with open ("D-large.in", "r") as myfile:
    data=myfile.readlines()
myfile.close()

counter = 0
for d in data:
    if str(d[len(d)-1:len(d)+1]) == "\n":
        data[counter] = d[:len(d)-1]
    counter +=1


numData = int(data[0])
del data[0]
for i in range(0, numData):
    numBlocks = int(data[0])
    del data[0]
    naomiblock = data[0].split()
    del data[0]
    kenblock = data[0].split()
    del data[0]
    naomiblock = [ float(x) for x in naomiblock ]
    kenblock = [ float(x) for x in kenblock ]
    naomiblock.sort()
    naomiblock.reverse()
    kenblock.sort()
    kenblock.reverse()

    #Deceitful War
    decPoints = 0
    countoff = 0
    for j in range(0, numBlocks):
        if naomiblock[j-countoff]>kenblock[j]:
            decPoints +=1
        else:
            countoff+=1
    
    #Optimal War
    naomiblock.reverse()
    kenblock.reverse()
    c1 = 0
    while len(kenblock)>0:

        c2 = 0
        countstop = -1
        for j in kenblock:
            if j>naomiblock[c1] and countstop == -1:
                countstop = c2
            c2+=1
        
        if countstop>=0:
            del kenblock[0:countstop+1]
        else:
            del kenblock[0:]
            c1-=1

        c1 += 1
            
    
            



    print "Case #"+str(i+1)+": "+str(decPoints)+" "+str(len(naomiblock)-c1)


