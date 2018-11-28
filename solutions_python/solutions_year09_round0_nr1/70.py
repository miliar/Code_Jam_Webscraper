'''
Google Code Jam 2009
Qualification Round
A. Alien Language

@author: Samuel Spiza
'''

def pattern2Array(pattern):
    tempArray = []
    for tempPattern in pattern.split(")"):
        tempPart = tempPattern.split("(")
        tempArray.extend([[tempPart[0][x]] for x in range(len(tempPart[0]))])
        if 1 < len(tempPart):
            tempArray.append([tempPart[1][x] for x in range(len(tempPart[1]))])
    return tempArray

#fileName = "A-small-practice.in"
#fileName = "A-small-attempt0.in"
fileName = "A-large.in"
file = open(fileName, "r")

words = []
patterns = []
i = 1

for line in file:
    if i == 1:
        tempArray = line.strip().split()
        L = int(tempArray[0])
        D = int(tempArray[1])
        N = int(tempArray[2])
    elif 1 < i and i <= 1 + D:
        words.append(line.strip())
    elif 1 + D < i:
        patterns.append(pattern2Array(line.strip()))
    i = i + 1

file.close()

#print words
#print patterns


string = ""
for n in range(N):
    tempWords = words[:]
    d = 0
    while d < len(tempWords):
        l = 0
        while l < L and tempWords[d][l] in patterns[n][l]:
            l = l + 1
        if l < L:
            tempWords.pop(d)
        else:
            d = d + 1
    string = string + "Case #" + str(n + 1) + ": " + str(len(tempWords)) + "\n"
    
file = open(fileName.rsplit(".", 1)[0] + ".out", "w")
file.write(string.strip())
file.close()
