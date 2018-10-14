f = open('C:\\Users\\fishbeinb\\Documents\\hw6.txt', 'r')
lineArr=f.read().split('\n')
n = 0
for x in range(int(lineArr[n])):
    templist = []
    templist2 = []
    n = n + 1
    possition = 1
    temp = int(lineArr[n])
    for y in range(4):
        n = n + 1
        if possition == temp:
            templist = lineArr[n].split()
        possition = possition + 1
    n = n + 1
    possition = 1
    temp = int(lineArr[n])
    for y in range(4):
        n = n + 1
        if possition == temp:
            templist2 = lineArr[n].split()
        possition = possition + 1
    if len(list(set(templist2) & set(templist))) == 0:
        print "Case #"+str(x+1)+": Volunteer cheated!"
    elif len(list(set(templist2) & set(templist))) == 1:
        print "Case #"+str(x+1)+": " + str(list(set(templist2) & set(templist))[0])
    else:
        print "Case #"+str(x+1)+": Bad magician!"
