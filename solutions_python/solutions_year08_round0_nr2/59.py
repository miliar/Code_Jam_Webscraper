def sortlist(list):
    list = [(10000*i+100*j+k,i,j,k)for i,j,k in list]
    list.sort()
    list=[(i,j,k) for h,i,j,k in list]
    return list

input = open("input.txt").readlines()
output = open("output.txt", "w")
for i in range(len(input)):
    if input[i][-1] == '\n':
        input[i] = input[i][:-1]

nOfCases = int(input[0])
cursor = 1

for casecount in range(nOfCases):
    turnaround = int(input[cursor])
    cursor+=1
    
    nOfA, nOfB = input[cursor].split()
    nOfA, nOfB = int(nOfA), int(nOfB)
    cursor+=1
    
    listA, listB = [], []
    for count in range(nOfA):
        depart, arrive = input[cursor].split()  
        
        depart=depart.split(':')
        depart[0],depart[1] = int(depart[0]),int(depart[1])
        listA.append((depart[0], depart[1], 1));
        
        arrive = arrive.split(':')
        arrive[0],arrive[1] = int(arrive[0]),int(arrive[1])
        arrive[0]+=(arrive[1]+turnaround) / 60;
        arrive[1]=(arrive[1]+turnaround) % 60;
        listB.append((arrive[0], arrive[1], -1))
        cursor +=1
        
    for count in range(nOfB):
        depart, arrive = input[cursor].split()

        depart=depart.split(':')
        depart[0],depart[1] = int(depart[0]),int(depart[1])
        listB.append((depart[0], depart[1], 1));

        arrive = arrive.split(':')
        arrive[0],arrive[1] = int(arrive[0]),int(arrive[1])
        arrive[0]+=(arrive[1]+turnaround) / 60;
        arrive[1]=(arrive[1]+turnaround) % 60;
        listA.append((arrive[0], arrive[1], -1))

        cursor+=1
    listA = sortlist(listA)
    listB = sortlist(listB)

    resultA=0
    idles = 0
    for temp in listA:
        if temp[2] == -1:
            idles +=1
        else:
            if (idles) == 0:
                resultA += 1
            else:
                idles -= 1

    resultB=0
    idles = 0
    for temp in listB:
        if temp[2] == -1:
            idles +=1
        else:
            if (idles) == 0:
                resultB += 1
            else:
                idles -= 1
    
    print >> output , "Case #" + str(casecount+1) + ": "+ str(resultA) + " "+ str(resultB)
    print "Case #" + str(casecount+1) + ": "+ str(resultA) + " "+ str(resultB)
