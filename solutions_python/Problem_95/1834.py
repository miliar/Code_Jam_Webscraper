xlate = {}
reverseXlate = {}

def buildDictionary(inputX, outputX):
    count = 0
    for c in inputX:
        xlate[c] = outputX[count]
        reverseXlate[outputX[count]] = c
        count = count + 1


def translate(inputX):
    output = []
    for c in inputX:
        if c != "\n":
            if c in xlate:
                output.append(xlate[c])
            else:
                output.append("X")
                
    return ''.join(output)

def reverseTranslate(outputX):
    input = []
    
    for c in enumerate(outputX):
        input.append(reverseXlate[c])

    return ''.join(input)


def runTest():
    f = open('/Users/bavetta/Desktop/code jam/A-small-attempt1 (1).in', 'r')
    numberOfLines = int(f.readline())
    numberOfLines
    test = 10
    test
    for i in range(numberOfLines):
        output = ["Case #"]
        output.append(str(i+1))
        output.append(": ")
        input = f.readline()
        output.append(translate(input))
        output = ''.join(output)

        print(output)

buildDictionary("a","y")
buildDictionary("o","e")
buildDictionary("z","q")
buildDictionary("q","z")
buildDictionary("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand")
buildDictionary("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities")
buildDictionary("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up")

runTest()

