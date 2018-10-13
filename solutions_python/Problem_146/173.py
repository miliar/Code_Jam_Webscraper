import math
import itertools

strings = []
letterDict = {}

def checkString(perm):
    full = ''
    letters = {}
    for word in perm:
        full += word
    prev = ''
    for letter in full:
        if letter != prev:
            if letter in letters:
                return False
            letters[letter] = 0
        prev = letter
    return True

def test():
    correct = 0
    for perm in itertools.permutations(strings):
        if checkString(perm):
            correct += 1
    return correct

def checkValid():
    letterPairs = {}
    for word in strings:
        x = 1
        startingLetter = word[0]
        endingLetter = word[len(word)-1]
        same = (startingLetter == endingLetter)
        prevLetter = word[0]
        while x < len(word)-1:
            if word[x] != prevLetter:
                if same:
                    return False
                if word[x] != endingLetter and word[x] in letterDict:
                    return False
                if word[x] != endingLetter:
                    letterDict[word[x]] = {}
            prevLetter = word[x]
            x += 1
        if same:
            if startingLetter in letterDict:
                if 'flex' in letterDict[startingLetter]:
                    letterDict[startingLetter]['flex'] += 1
                else:
                    letterDict[startingLetter]['flex'] = 1
            else:
                letterDict[startingLetter] = {'flex': 1}
        else:
            if (endingLetter, startingLetter) in letterPairs:
                return False
            letterPairs[(startingLetter, endingLetter)] = 1
            if startingLetter in letterDict:
                if 'start' in letterDict[startingLetter]:
                    return False
                else:
                    letterDict[startingLetter]['start'] = 1
            else:
                letterDict[startingLetter] = {'start': 1}
            if endingLetter in letterDict:
                if 'end' in letterDict[endingLetter]:
                    return False
                else:
                    letterDict[endingLetter]['end'] = 1   
            else:
                letterDict[endingLetter] = {'end': 1}
    return True    

f = open('B-small-attempt3.in', 'r')
numCases = int(f.readline())
x = 1
while x <= numCases:
    numCars = int(f.readline())
    letterDict = {}
    line = f.readline()
    y = 0
    orderings = 1
    strings = []
    while y < numCars:
        strings.append(line.split()[y])
        y += 1
    if not checkValid():
        print "Case #" + str(x) + ": 0"
        x += 1
        continue
    else:
        entities = numCars
        for letter in letterDict:
            if 'start' in letterDict[letter] and 'end' in letterDict[letter]:
                entities -= 1
            if ('start' in letterDict[letter] or 'end' in letterDict[letter]) and 'flex' in letterDict[letter]:
                entities -= 1
            if 'flex' in letterDict[letter]:
                orderings *= math.factorial(letterDict[letter]['flex'])
                entities -= (letterDict[letter]['flex']-1)
        orderings *= math.factorial(entities)
        print "Case #" + str(x) + ": " + str(orderings)
    x += 1