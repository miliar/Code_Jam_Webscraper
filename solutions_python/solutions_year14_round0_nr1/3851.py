from functools import partial

def readMind(previousRow, currentRow):
    for x in currentRow:
        if x in previousRow:
            return x
    

def volunteerCheated(previousRow, currentRow):
    found = 0
    for x in currentRow:
        if x in previousRow:
            found +=1
    return found == 0

def lineIsGood(previousRow, currentRow):
##    print('prev')
##    print(previousRow)
##    print('curr')
##    print(currentRow)
    found = 0
    #for x in map(lambda x: x.strip(), currentRow.split(' ')):
    for x in currentRow:
        if x in previousRow:
            found += 1
##    print(found)
    return found == 1
    
def solve(lines):
    firstChoice = int(lines[0])
    secondChoice = int(lines[5])
    firstRow = list(map(lambda x: x.strip(), lines[firstChoice].split(' ')))
    secondRow = list(map(lambda x: x.strip(), lines[5+secondChoice].split(' ')))
    if volunteerCheated(firstRow, secondRow):
        return 'Volunteer cheated!'
    if lineIsGood(firstRow,secondRow):
        return readMind(firstRow,secondRow)
    else:
    #if (not all(map (partial(lineIsGood, firstRow),lines[6:10]))):
        return 'Bad magician!'
    return readMind(firstRow,secondRow)

#with open("input.txt") as f:
with open("A-small-attempt5.in") as f:
    content = f.readlines()
    cases = int(content[0])
    i = 1
    while i <= cases:
        print ("Case #" + str(i) + ': ' + solve(content[1+(10*(i-1)):11+(10*(i-1))]))
        i +=1
        
