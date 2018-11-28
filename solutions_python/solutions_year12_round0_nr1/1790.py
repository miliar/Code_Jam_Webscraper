#! /usr/local/bin/python
import sys
import string

def openFile(fileName):
    file = open(fileName, 'r')
    lines = file.readlines()
    file.close()
    return lines

def formatLines(lines):
    y = 0
    while y < len(lines):
        lines[y] = lines[y].rstrip('\n')
        y +=1
    return lines

def formatOutput(lines):
    y = 0
    while y < len(lines):
        lines[y] = lines[y][9:]
        y +=1
    return lines
   
googEng={'y':'a','e':'o', 'q':'z'}

fileNameInput = '/Users/erynmaynard/Desktop/GoogleCodeJam/input.txt'
inputLines = openFile(fileNameInput)
inputLines = formatLines(inputLines)
inputLines = inputLines[1:]

fileNameOutput = '/Users/erynmaynard/Desktop/GoogleCodeJam/output.txt'
outputLines = openFile(fileNameOutput)
outputLines = formatOutput(formatLines(outputLines))

x = 0
while x < len(inputLines):
    inputCase = inputLines[x]
    outputCase = outputLines[x]
    y = 0
    while y < len(inputCase):
        inputLetter = inputCase[y]
        if not googEng.has_key(inputLetter):
            googEng[inputLetter] = outputCase[y]
        y += 1
    x += 1

leftOver = []
possibleLetters = string.ascii_lowercase
for q in string.ascii_lowercase:
    if not googEng.has_key(q):
        leftOver.append(q)
    else:
        possibleLetters = possibleLetters.replace(googEng[q], '')
googEng[leftOver[0]] = possibleLetters

fileNameInputTry = '/Users/erynmaynard/Desktop/GoogleCodeJam/A-small-attempt3.in'
inputLinesTry = openFile(fileNameInputTry)
inputLinesTry = formatLines(inputLinesTry)
inputLinesTry = inputLinesTry[1:]

print(googEng)

fileNameOutput = '/Users/erynmaynard/Desktop/GoogleCodeJam/finalOutput.in'
output = open(fileNameOutput, 'w')
z=1
for x in inputLinesTry:
    word = ''
    for y in x:
        if not googEng.has_key(y):
            print y
        word += googEng.get(y)
    output.write("Case #" + str(z) + ": " + word)
    print("Case #" + str(z) + ": " + word)
    z +=1
output.close()
