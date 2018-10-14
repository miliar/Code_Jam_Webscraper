def readInput(fileName):
    fileName=open(fileName)
    lists=fileName.read().split()
    caseNum=lists[0]
    fileName.close()

    pointer=1
    caseList=[]
    lenList=[]
    
    while True:
        if pointer>=len(lists): break
        length=int(lists[pointer])
        pointer+=1
        lenList.append(length)
        case=lists[pointer]
        caseList.append(case)
        pointer+=1
        
    return caseList,lenList,caseNum

caseList,lenList,caseNum=readInput('A-large.in')

outfile=open('out.txt','w')
for i in range(int(caseNum)):
    
    outfile.write('Case #'+str(i+1)+': ')

    frd=0
    frds=0
    aud=0
    string=caseList[i]
 
    for j in range(len(string)):
        frd=0

        if aud>=int(j):
            aud+=int(string[j])
        else:
            frd+=int(j)-aud
            aud+=frd
            aud+=int(string[j])
            frds+=frd
        

    outfile.write(str(frds))
    outfile.write('\n')
outfile.close()
        

