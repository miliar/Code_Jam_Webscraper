fin=open("test.txt", "r")
data=fin.readlines()
i=1
testcases=int(data[0])
#print data
#print "testcases", testcases
while (i<(2*testcases)):

    dataline=data[i].split(" ")
    for j in range(len(dataline)):
        dataline[j]=int(dataline[j])
    #print "r,k,n", dataline, i
    
    queue=data[i+1].split(" ")
    for j in range(len(queue)):
        queue[j]=int(queue[j])
    #print "queue", queue, i

    i=i+2

    r=dataline[0]
    k=dataline[1]
    line=queue
    
    overall=0
    for j in range(r):
        people=0
        movements=0
        while ((people+line[movements])<=k):
            people=people+line[movements]
            movements=movements+1
            if(movements>(len(line)-1)):
                break
            #print people, k
        line=line[movements:]+line[:movements]
        overall=overall+people
       # print line
        
    print "Case #"+str(i/2)+": "+str(overall)
