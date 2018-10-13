
inputFile = open('A-small-attempt0.in','r')
outputFile = open('A-small-attempt0.ou','w')


numTest = int(inputFile.readline())
for testid in range(1,numTest+1):
    row1 = int(inputFile.readline())
##    print(row1)
    for row in range(0,4):
        line = inputFile.readline()
        if row==row1-1:
            set1 = set([int(s) for s in line.split()])
##            print(set1)
    row2 = int(inputFile.readline())
##    print(row2)
    for row in range(0,4):
        line = inputFile.readline()
        if row==row2-1:
            set2 = set([int(s) for s in line.split()])
##            print(set2)

    count = 0
    
    for number in set1:
        if number in set2:
            count = count+1
            chosennumber = number

    if count==1:
        print('Case #',testid,': ',chosennumber, sep='',file=outputFile)
    elif count==0:
        print('Case #',testid,': Volunteer cheated!', sep='',file=outputFile)
    elif count>1:
        print('Case #',testid,': Bad magician!', sep='',file=outputFile)


outputFile.close()
    
        
