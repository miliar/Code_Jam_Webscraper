fo = open("A-small-attempt4.in")
fo2 = open("output.txt", mode='w')
tests = eval(fo.readline())

output=[];
for x in range(1,tests+1):
    listS = []
    listS2=[]
    row1=eval(fo.readline())

    for i in range(4):
        text=fo.readline()[:-1]

        if i+1==row1:
            listS.extend(text.split(" "))
    row2=eval(fo.readline())
    for i in range(4):
        text=fo.readline()[:-1]
        if i+1==row2:
            listS2.extend(text.split(" "))

    newList= []
    for y in listS:
        if y in listS2:
            newList.append(y)

    if len(newList) > 1:
        print("Case #",x,": Bad magician!", sep="")
        output.append("Case #"+str(x)+": Bad magician!")
    if len(newList) == 1:
        print("Case #",x,": ",newList[0], sep="")
        output.append("Case #"+str(x)+": "+str(newList[0]))
    if len(newList) == 0:
        print("Case #",x,": Volunteer cheated!", sep="")
        output.append("Case #"+str(x)+": Volunteer cheated!")

    output.append("\n")
fo2.writelines(output)

