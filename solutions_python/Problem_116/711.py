import re, itertools, math

input = open('C:\\Users\\Adam\\Downloads\\A-large.in', 'r')
#input = open('C:\\Python27\\CodeJam\\Qualification 2013\\inputs.txt', 'r')
output = open('C:\\Python27\\CodeJam\\Qualification 2013\\outputs.out', 'w')

cases = int(input.readline())
case = 1

wins = {
           "OOOO": "O Won",
           "XXXX": "X Won"
       }

while case <= cases:
    l = 1
    finished = True
    while l <= 4:
        line = input.readline()
        if l == 1:
            if line.find('.') != -1:
                finished = False
            h1 = line[0:4]
            v1 = line[0]
            v2 = line[1]
            v3 = line[2]
            v4 = line[3]
            d1 = line[0]
            d2 = line[3]
        elif l == 2:
            if line.find('.') != -1:
                finished = False
            h2 = line[0:4]
            v1 += line[0]
            v2 += line[1]
            v3 += line[2]
            v4 += line[3]
            d1 += line[1]
            d2 += line[2]
        elif l == 3:
            if line.find('.') != -1:
                finished = False
            h3 = line[0:4]
            v1 += line[0]
            v2 += line[1]
            v3 += line[2]
            v4 += line[3]
            d1 += line[2]
            d2 += line[1]
        elif l == 4:
            if line.find('.') != -1:
                finished = False
            h4 = line[0:4]
            v1 += line[0]
            v2 += line[1]
            v3 += line[2]
            v4 += line[3]
            d1 += line[3]
            d2 += line[0]
        l = l + 1
    input.readline() #skip past the blank line in the input
    checks = [h1,h2,h3,h4,v1,v2,v3,v4,d1,d2]
    result = ""
    x = 1
    for check in checks:
        if check.replace('T', 'X') == "XXXX":
            result = "X won"
            break
        elif check.replace('T', 'O') == "OOOO":
            result = "O won"
            break
    if not result:
        if not finished:
            result = "Game has not completed"
        else:
            result = "Draw"
    result = "Case #" + str(case) + ": " + result
    if case != cases:
        result = result + "\n"
    output.write(result)
    case += 1
output.close()
input.close()
            
