file=open('A-small-attempt0.in','r')
output=open('q1answer.out','w')
fileArray1=file.readlines()
fileArray2=[]
index=0
for i in fileArray1:
    fileArray2.append(i.split("\n"))

temp1=fileArray2.pop(0)

NumOfTests=int(temp1.pop(0))

while index<NumOfTests:
    firstArr=[]
    secondArr=[]
    temp2=fileArray2.pop(0)
    firstAns=int(temp2.pop(0))
    count=0
    while count<4:
        temp3=fileArray2.pop(0)
        firstArr.append(temp3.pop(0).split(" "))
        count=count+1
    temp4=fileArray2.pop(0)
    secondAns=int(temp4.pop(0))
    count=0
    while count<4:
        temp5=fileArray2.pop(0)
        secondArr.append(temp5.pop(0).split(" "))
        count=count+1
    finalCount=0
    for i in range(0,4):
        for j in range(0,4):          
            if int(firstArr[firstAns-1][i]) == int(secondArr[secondAns-1][j]):
                num=firstArr[firstAns-1][i]
                finalCount=finalCount+1
            
    #print(finalCount)
    if finalCount==0:
        output.writelines("Case #"+str(index+1)+": "+"Volunteer cheated!"+"\n")
    elif finalCount==1:
        output.writelines("Case #"+str(index+1)+": "+num+"\n")
    else:
        output.writelines("Case #"+str(index+1)+": "+"Bad magician!"+"\n")
        

        
    index=index+1
file.close()
output.close()
