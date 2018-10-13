inputFile = open("A-small-attempt1.in","r")
outputFile = open("A-small-output.txt","w")
t = int(inputFile.readline())
for i in range(1,t+1):
    row1 = int(inputFile.readline())-1
    fList = []
    for j in range(4):
        fList.append(map(int,inputFile.readline().split()))
    row2 = int(inputFile.readline())-1
    sList = []
    for j in range(4):
        sList.append(map(int,inputFile.readline().split()))
    ans = list(set(fList[row1])&set(sList[row2]))
    size = len(ans)
    sAns = "Case #"+str(i)+": "
    if size == 0:
        sAns += "Volunteer cheated!"
    elif size == 1:
        sAns += str(ans[0])
    else:
        sAns += "Bad magician!"
    outputFile.write(sAns+'\n')
outputFile.close()

