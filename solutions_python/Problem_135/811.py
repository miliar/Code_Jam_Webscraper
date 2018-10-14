fileOpen=open("magic1.in","r+")
fileOpen2=open("magic.txt","w+")
testCases=int(fileOpen.readline())
for i in range(1,testCases+1):
    matches=0
    matching=0
    row1=int(fileOpen.readline())
    order1 =[]
    order1.append(fileOpen.readline().split())
    order1.append(fileOpen.readline().split())
    order1.append(fileOpen.readline().split())
    order1.append(fileOpen.readline().split())
    row2=int(fileOpen.readline())
    order2=[]
    order2.append(fileOpen.readline().split())
    order2.append(fileOpen.readline().split())
    order2.append(fileOpen.readline().split())
    order2.append(fileOpen.readline().split())
    for j in range(0,4):
        if(order1[row1-1][j] in order2[row2-1]):
            matching=int(order1[row1-1][j])
            matches=matches+1
    if(matches==1):
        fileOpen2.write('Case #%d: %d\n'%(i,matching))
    elif(matches>1):
        fileOpen2.write('Case #%d: Bad magician!\n'%(i))
    else:
        fileOpen2.write('Case #%d: Volunteer cheated!\n'%(i))

            
    