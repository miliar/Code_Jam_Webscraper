def MagicTrick(inputfile, outputfile, griddim):
    inputdata = open(inputfile, "r")
    outputdata = open(outputfile, "w")
    T = int(inputdata.readline())
    for case in range(T):
        firstrow = int(inputdata.readline())
        firstschikking = [inputdata.readline().split() for x in range(griddim)]
        secondrow = int(inputdata.readline())
        secondschikking = [inputdata.readline().split() for x in range(griddim)]
        #print firstrow, firstschikking, secondrow, secondschikking
        outputzin = compareTwoLists(firstschikking[firstrow-1],secondschikking[secondrow-1]) 
        outputdata.write("Case #" + str(case+1) + ": " + outputzin + "\n")
        print 
    inputdata.close()
    outputdata.close()
def compareTwoLists(listOne, listTwo):
    IsFound = False
    outputzin = "Volunteer cheated!"
    for intRowOne in listOne:
        for intRowTwo in listTwo:
            if intRowOne == intRowTwo:
                outputzin = str(intRowOne)
                if IsFound:
                    outputzin = "Bad magician!"
                    break
                IsFound = True
            #print intRowOne, intRowTwo, IsFound
    return outputzin

def checkoutput(fileone, filetwo):
    one = open(fileone, 'r')
    two = open(filetwo, 'r')
    fout = False
    print "checking..."
    for lineone in one:
        linetwo =two.readline()
        #print lineone, linetwo
        if lineone != linetwo:
            fout = True
            print "Fout!!! \n", lineone, linetwo
            break
    if not fout:
        print "alles in orde"

