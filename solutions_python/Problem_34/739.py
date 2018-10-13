import re


def searchTokens(input, alienDict):
    combinations = []
    matches = 0

    input = [re.sub(r'\(|\)', '', token) for token in input]

    for word, value in alienDict.items():
        noMatch = False

        for i in range(len(word)):
            if input[i].find(word[i]) != -1:
                continue
            else:
                noMatch = True
                break

        if not noMatch:
            matches += 1

    return matches


def parseFile(file):
    metaData = []
    alienWords = {}
    testCases = []

    with open(file) as inputFile:
        firstLine = True
        wordCounter = 0

        for line in inputFile:
            line = line.strip()
            if firstLine:
                #Get metadata L (length), D (words), N (test cases)
                metaData = line.split(" ")
                firstLine = False
            else:
                #Get alien words
                if wordCounter < int(metaData[1]): 
                    wordCounter += 1
                    alienWords[line] = 0 
                else:
                    #Get test cases
                    testCases.append(tokenizer.findall(line))


    aCase = 0

    for item in testCases:
        aCase += 1

        if re.search(r"\(|\)", "".join(item)):
            outfile.write("Case #" + str(aCase) + ": " + str(searchTokens(item, alienWords)) + "\n")
        else:
            count = 0

            if alienWords.has_key("".join(item)):
                count = 1

            outfile.write("Case #" + str(aCase) + ": " + str(count) + "\n")


tokenizer = re.compile("\([^)]+\)|\w")

outfile = open("alien_language_result.txt", "w")
#parseFile("A-small-attempt2.in")
parseFile("A-large.in")
#parseFile("A-small.in")
outfile.close()
