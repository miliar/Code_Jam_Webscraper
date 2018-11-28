mainMatrix = [     [1,1,1,1],    [1,1,1,1],   [1,1,1,1],   [1,1,1,1]        ]

def dataProcessor(line1,line2,line3,line4):
    counter = 0
    for i in line1:
        mainMatrix[0][counter] = int(i)
        counter += 1
    counter = 0
    
    for i in line2:
        mainMatrix[1][counter] = int(i)
        counter += 1
    counter = 0
    
    for i in line3:
        mainMatrix[2][counter] = int(i)
        counter += 1
    counter = 0
    for i in line4:
        mainMatrix[3][counter] = int(i)
        counter += 1
    
        
        
    
def trickCracker(listOne, listTwo, poryadok):
    counter = 0
    element = None
    for item in listTwo:
        if item in listOne:
            counter += 1
            element = item

    if counter == 0:
        return "Case #" + str(poryadok) +":" + " " + "Volunteer cheated!"
    elif counter ==  1:
        return "Case #" + str(poryadok) +":" + " "+ str(element)
        
    elif counter >1:
        return "Case #" + str(poryadok) +":" + " " +"Bad Magician!"
    


file = open("/home/dmitrii/Coding/Google JAM/A-small-attempt1.in", "r")
dataList = []
for line in file:
    dataList.append(line.split())
file.close()
    
numTimes = int(dataList[0][0])

file = open('/home/dmitrii/Coding/Google JAM/output.out','w')
for i in range(numTimes):
    answer1 = int(dataList[1+(i*10)][0]) - 1
    
    list1 = dataList[2+(i*10)]
    list2 = dataList[3+(i*10)]
    list3 = dataList[4+(i*10)]
    list4 = dataList[5+(i*10)]
    
    dataProcessor(list1,list2,list3,list4)
    firstList = mainMatrix[answer1].copy()
    
    
    answer2 = int(dataList[6+(i*10)][0]) - 1
    
    
    list1 = dataList[7+(i*10)]
    list2 = dataList[8+(i*10)]
    list3 = dataList[9+(i*10)]
    list4 = dataList[10+(i*10)]
    
    dataProcessor(list1,list2,list3,list4)
    secondList = mainMatrix[answer2].copy()
    
    
    file.write(trickCracker(firstList, secondList,i+1)+'\n')


file.close()
    


