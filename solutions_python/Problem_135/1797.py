#Reading and opening file in data
with open ("A-small-attempt6.in", "r") as myfile:
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
    findrow1 = int(data[0])
    findrow2 = int(data[5])
    row1 = data[findrow1]
    row2 = data[findrow2+5]
    row1 = row1.split()
    row2 = row2.split()
    del data[0:10]
    mergelist = row1+row2
    answerlist = []
    answer = ""
    for j in mergelist:
        if j not in answerlist:
            answerlist.append(j)
        else:
            answer = j

    if len(answerlist) == 8:
        print "Case #"+str(i+1)+": Volunteer cheated!"
    if len(answerlist) == 7:
        print "Case #"+str(i+1)+": "+answer
    if len(answerlist)<7:
        print "Case #"+str(i+1)+": Bad magician!" 
