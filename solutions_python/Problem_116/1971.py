#!/usr/bin/python

def checkVictory(var,input):
    for line in input:
        cnt = line.count(var)
        if cnt is 3 and 'T' in line:
            return True
        if cnt is 4:
            return True
    return False

def checkCompletion(input):
    return '.' in [x[y] for x in input for y in range(0,4)]

fd = open('input.txt','r')
count = int(fd.readline().strip())
iterator = 0
while iterator < count:
    iterator += 1
    input = []
    processing = []
    input.append(list(fd.readline().strip()))
    input.append(list(fd.readline().strip()))
    input.append(list(fd.readline().strip()))
    input.append(list(fd.readline().strip()))
    output = "Draw"
    #Reverse diag
    processing.append([input[3-x][x] for x in range(0,4)])
    #Diag
    processing.append([input[x][x] for x in range(0,4)])
    #Verticle
    trash = [processing.append([x[i] for x in input]) for i in range(0,4)]
    for x in processing:
        input.append(x)
    if checkVictory("X",input):
        output = "X won"
    elif checkVictory("O",input):
        output = "O won"
    elif checkCompletion(input):
        output = "Game has not completed"

    trash = fd.readline()
    # Tell us what you found
    output = "Case #%s: %s" % (iterator,output)
    print output
