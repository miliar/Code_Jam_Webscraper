def checkRows(matrix, initial):
    afterCutMatrix = []
    for i, row in enumerate(matrix):
        initValue = row[0]
        if row != [initValue]*len(row):
            for j, value in enumerate(row):
                columnJ = [x[j] for x in matrix]
                maxNum = max(columnJ)
                
                if value < maxNum:
                    return False
    return True


def lawnmower(inputText, initial):
    outPut = open("output","w")
    inputText = open(inputText)
    numOfCases =  int(inputText.readline()[:-1])

    for case in range(numOfCases):

        line = map(int, inputText.readline()[:-1].split(" "))
        rows =  line[0]
        columns =  line[1]
        
        matrix = []
        for i in range(rows):
            tempRow = map(int, inputText.readline()[:-1].split(" "))
            row = [x for x in tempRow]
            matrix.append(row)


        if checkRows(matrix, initial):
            outPut.write("Case #"+str(case + 1)+": YES\n")      
        else:
            outPut.write("Case #"+str(case + 1)+": NO\n")      

if __name__ == "__main__":
    a = lawnmower("B-small-attempt1.in", 2)
    print "DONE" 
