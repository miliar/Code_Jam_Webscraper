
def serializeInputFile(inputFile):
    inputList=[]
    f=open(inputFile)
    length=int(f.readline())
    while length>0:
        string=f.readline().split()[1]
        li = []
        for ch in string:
            li.append(int(ch))
        inputList.append(li)
        length -= 1
    return inputList

def createOutputFile(outputList,outputFile):
    start = 1
    f = open(outputFile,"w")
    for data in outputList:
        f.write("Case #" + str(start) + ": " + str(data) + "\n")
        start+=1

inputFile=r"C:\Users\jaias_000\Desktop\A-large.in"
outputFile=r"C:\Users\jaias_000\Desktop\output.txt"
outputList=[]
inputList = serializeInputFile(inputFile)
for input in inputList:
    totalPeople = 0
    requiredFriend = 0
    for index in range(len(input)):
        if((totalPeople + requiredFriend) < index):
            requiredFriend += index - (totalPeople + requiredFriend)
        totalPeople += input[index]
    outputList.append(requiredFriend)
createOutputFile(outputList,outputFile)