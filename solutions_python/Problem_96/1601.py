
__author__="reszegtivadar"
__date__ ="$Apr 14, 2012 7:06:48 PM$"

if __name__ == "__main__":
    print "Hello";


def giveBackPossibleTriplet(sum):
    posibleTrip = [0,0,0]
    couldBeSurpizing = 0; # means no
    if (sum % 3 == 0):
        posibleTrip = [sum/3, sum/3, sum/3]
        couldBeSurpizing = 1; # means yes
    else:
        newSum = sum - sum/3
        if (newSum % 2 == 0):
            posibleTrip = [newSum/2, newSum/2, sum/3]
        else:
            posibleTrip = [newSum - newSum/2, newSum/2, sum/3]
    posibleTrip.append(couldBeSurpizing)
    return posibleTrip

def calculate(maxResult, nrSurpize, rArray):
    
    tripArray = []
    sorted(rArray, reverse = True)
    for i in range(len(rArray)):
        triplet = giveBackPossibleTriplet(rArray[i])
        tripArray.append(triplet)

    remainNrSurp = nrSurpize
    for i in range(len(tripArray)):
        #if (tripArray[i][3] != 1):
        if ((tripArray[i][0] < maxResult) and (tripArray[i][0] + 1 >= maxResult)):
            if (tripArray[i][0] == tripArray[i][1]):
                if (remainNrSurp > 0  and (tripArray[i][1] - 1) >= 0):
                    tripArray[i][0] = tripArray[i][0] + 1
                    tripArray[i][1] = tripArray[i][1] - 1
                    remainNrSurp -= 1


#    for i in range(len(tripArray)):
#        if (tripArray[i][3] == 1):
#            if (remainNrSurp > 0  and (tripArray[i][2] - 1) >= 0):
#                tripArray[i][0] = tripArray[i][0] + 1
#                tripArray[i][2] = tripArray[i][2] - 1
#                remainNrSurp -= 1

    print maxResult, nrSurpize, rArray, tripArray


    res = 0
    for i in range(len(tripArray)):
        if (tripArray[i][0] >= maxResult):
            res += 1
    return res
print 22, giveBackPossibleTriplet(22),


from textFile import TextFile
#input = TextFile('2012_B_input_test')
#output = TextFile('2012_B_output_test')


input = TextFile('B-large.in')
output = TextFile('B-large.out')


lines = input.readLinesFromFile()

numberOfLines = int (lines[0])
print numberOfLines
for i in range(numberOfLines):
    resultRow = "Case #"+str(i+1)+": "

    lineArray = lines[i+1].split(" ")
    nrOfGoglers = int (lineArray[0])
    nrOfSuprizing = int (lineArray[1])
    maxResult = int (lineArray[2])

    resultsArray = []
    for j in range(nrOfGoglers):
        resultsArray.append(int (lineArray[j+3]))
    res = calculate(maxResult, nrOfSuprizing, resultsArray)

    resultRow = resultRow + str (res) + "\n"
    print resultRow
    if (i == 0):
        output.writeToFile(resultRow)
    else:
        output.appendToFile(resultRow)

