import sys, collections, math

stored_values = {}
best_splits = {}

def minutesRequired (count, pancakes):
    if count in stored_values:
        lists = stored_values[count]
        for array in lists:
            if collections.Counter(array["list"]) == collections.Counter(pancakes):
                return array["value"]
    #print(str(count) + ": " + str(pancakes))
    maxElem = max(pancakes)
    if maxElem == 1:
        value = 1
    else:
        allowedArray = []
        for elem in pancakes:
            if (elem - 1) != 0:
                allowedArray.append(elem - 1)
        #print(str(len(allowedArray)) + ": " + str(allowedArray))
        specialArray = list(pancakes)
        maxElement = max(specialArray)
        specialArray.remove(maxElement)
        specialArray.extend(best_splits[maxElement])
        value = min(minutesRequired(len(allowedArray), allowedArray)+1, minutesRequired(len(specialArray), specialArray)+1)
    result = {}
    result["list"] = pancakes
    result["value"] = value
    if count not in stored_values:
        stored_values[count] = []
    stored_values[count].append(result)
    return value


if __name__ == "__main__":
    best_splits[2] = [1, 1]
    best_splits[3] = [1, 2]
    best_splits[4] = [2, 2]
    best_splits[5] = [3, 2]
    best_splits[6] = [3, 3]
    best_splits[7] = [3, 4]
    best_splits[8] = [4, 4]
    best_splits[9] = [3, 6]
    inputFile = open(sys.argv[1], 'r')
    outputFile = open("final-output.txt", 'w')
    testCases = inputFile.readline()
    testCases = int(testCases.rstrip(" \t\n\r"))
    for i in range(0, testCases):
        count = int(inputFile.readline().rstrip(" \t\n\r"))
        line = inputFile.readline().rstrip(" \t\n\r")
        pancakes = line.split(" ")
        pancakes = [ int(x) for x in pancakes ]
        value = minutesRequired(count, pancakes)
        outputFile.write("Case #" + str(i+1) + ": " + str(value) + "\n")
    inputFile.close()
    outputFile.close()
