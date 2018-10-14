import sys

#Check last two
def combine(combos, fullList):
    if (len(fullList) <= 1):
        return
    elif ((fullList[-1] + fullList[-2]) in combos):
        #print "COMBINATION!!!"
        char1 = fullList.pop()
        char2 = fullList.pop()
        fullList.append(combos[char1 + char2])
        return




def oppose(opposed, fullList):
    if (len(fullList) <= 1):
        return
    char1 = fullList.pop()
    if (char1 in opposed):
        for char2 in opposed[char1]:
            if char2 in fullList: #then we need to clear it
                del fullList[:]
                #print "DELETED!!!"
                return

    fullList.append(char1)
    return





if __name__ == '__main__':

    for arg in sys.argv:
        inputfilename = arg;

    #check if input string is null???

    inputfile = open(inputfilename, 'r')

    outputfile = open(inputfilename + ".out", 'w')
    numberofsets = int(inputfile.readline())

    for m in range(numberofsets):
        line = inputfile.readline().rstrip('\r\n').split(' ')

        C = int(line[0])
        #print "C: " + str(C)
        combos = dict()
        for combineIndex in range(1, C + 1):
            ##print line[combineIndex]
            currentCombo = list(line[combineIndex])
            combos[currentCombo[0] + currentCombo[1]] = currentCombo[2]
            combos[currentCombo[1] + currentCombo[0]] = currentCombo[2]

            #combos.append(list(line[combineIndex]))

        ##print combos

        D = int(line[C + 1])
        #print "D: " + str(D)
        opposed = dict()
        for opposeIndex in range(C + 2, C + D + 2):
            #print line[opposeIndex]
            currentOpposed = list(line[opposeIndex])
            if (currentOpposed[0] in opposed):
                opposed[currentOpposed[0]].append(currentOpposed[1])
            else:
                opposed[currentOpposed[0]] = [currentOpposed[1]]


            if (currentOpposed[1] in opposed):
                opposed[currentOpposed[1]].append(currentOpposed[0])
            else:
                opposed[currentOpposed[1]] = [currentOpposed[0]]


        #print "opposed: "
        #print opposed


        N = int(line[C + D + 2])
        #print "N: " + str(N)
        invocation = list(line[C + D + 3])

        #print "Invocation: "
        #print invocation

        invoked = list()

        for i in invocation:
            invoked.append(i)
            combine(combos=combos, fullList = invoked)
            oppose(opposed=opposed, fullList = invoked)
            ##print "invoked "
            #print invoked





# 1) Check if there is a conversion
# 2) If there is a conversion





        outputline = "Case #" + str(m + 1) + ": ["
        for character in invoked:
            outputline += character + ', '
        outputline = outputline.rstrip(', ')
        outputline += ']\n'
        print outputline
        outputfile.write(outputline)


