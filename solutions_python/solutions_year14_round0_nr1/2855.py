# Rubens Pessoa de Barros Filho from Arapiraca, Brazil.

numOfTestCases = int(raw_input())
test = 1

while test <= numOfTestCases:
    
    possibilities = []
    answer1 = int(raw_input())
    firstLine1 = map(int, raw_input().split())
    secondLine1 = map(int, raw_input().split())
    thirdLine1 = map(int, raw_input().split())
    fourthLine1 = map(int, raw_input().split())
    
    answer2 = int(raw_input())
    firstLine2 = map(int, raw_input().split())
    secondLine2 = map(int, raw_input().split())
    thirdLine2 = map(int, raw_input().split())
    fourthLine2 = map(int, raw_input().split())
    
    if answer1 == 1:
        lineChoosen1 = firstLine1
    elif answer1 == 2:
        lineChoosen1 = secondLine1        
    elif answer1 == 3:
        lineChoosen1 = thirdLine1
    elif answer1 == 4:
        lineChoosen1 = fourthLine1
        
    if answer2 == 1:
        lineChoosen2 = firstLine2
    elif answer2 == 2:
        lineChoosen2 = secondLine2        
    elif answer2 == 3:
        lineChoosen2 = thirdLine2
    elif answer2 == 4:
        lineChoosen2 = fourthLine2
        
    for i in range(len(lineChoosen1)):
        for j in range(len(lineChoosen2)):
            if lineChoosen1[i] == lineChoosen2[j]:
                possibilities.append(lineChoosen1[i])
                
    
    if len(possibilities) == 1:
        print "Case #" + str(test) + ": %d" % (possibilities[0])
    elif len(possibilities) == 0:
        print "Case #" + str(test) + ": Volunteer cheated!"
    else:
        print "Case #" + str(test) + ": Bad magician!"
    
    
    test = test + 1
                
        
    