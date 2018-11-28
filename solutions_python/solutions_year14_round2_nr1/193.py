import math
f = open('A-large.in', 'r')
numCases = int(f.readline())
x = 1
while x <= numCases:
    numStrings = int(f.readline())
    y = 0
    words = []
    while y < numStrings:
        words.append(f.readline())
        y += 1
    wordCount = 0
    letters = []
    letterCounts = []
    match = True
    for word in words:
        if match is False:
            break
        letterCount = -1
        prevLetter = ""
        for letter in word:
            if letter == "\n":
                continue
            if letter != prevLetter:
                letterCount += 1
                if wordCount is 0:
                    letters.append(letter)
                    letterCounts.append([1])
                else:
                    if len(letters) == letterCount or letters[letterCount] != letter:
                        match = False
                        break
                    else:
                        letterCounts[letterCount].append(1)
            else:
                letterCounts[letterCount][wordCount] += 1
            prevLetter = letter
        if len(letters) != letterCount+1:
            match = False
            break
        wordCount += 1
    if not match:
        print "Case #" + str(x) + ": Fegla Won"
    else:
        totalDiff = 0
        for item in letterCounts:
            item = sorted(item)
            maximum = item[len(item)-1]
            y = 1
            best = maximum*len(item)
            counter = 0
            while y <= maximum:
                counter = 0
                for count in item:
                    counter += abs(count-y)
                if counter < best:
                    best = counter
                y += 1
            totalDiff += best
        print "Case #" + str(x) + ": " + str(totalDiff)
    x += 1