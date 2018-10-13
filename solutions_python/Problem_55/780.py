#Theme Park
fin = file("C-small.in")
case=0
end = int(fin.readline())
for x in range(0,end):
    case+=1
    line1 = fin.readline().replace("\n","")
    line2 = fin.readline().replace("\n","")
    g = line1.split(" ")
   
    R=int(g[0])
    k=int(g[1])
    N=int(g[2])
    h= line2.split(" ")
    
    queue=[]
    for num in h:
        queue.append(num)
    euros=0
    for times in range(0,R):
        spot=0
        sum1=0
        while (sum1<k):
            sum1+= int(queue[spot])
            if (sum1>k):
                sum1-=int(queue[spot])
                break
            spot+=1
            if spot==N:
                break
        euros += sum1
        temp=[]
        for y in range(0,spot):
            temp.append( queue[y])
        for lay in temp:
            queue.remove(lay)
        [queue.append(i) for i in temp]

    
    print "Case #"+str(case)+": " + str(euros)
        
