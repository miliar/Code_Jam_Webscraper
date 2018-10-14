#!/usr/bin/python

inp = open('small.in', 'r')
out = open('out', 'w')

times = int(inp.readline().strip())

i = 0

BAD = "Bad magician!"
CHEATED = "Volunteer cheated!"

while i < times:
    result = ""
    first = int(inp.readline().strip())
    firstA = []
    firstA.append(inp.readline().strip().split(' '))
    firstA.append(inp.readline().strip().split(' '))
    firstA.append(inp.readline().strip().split(' '))
    firstA.append(inp.readline().strip().split(' '))

    second = int(inp.readline().strip())
    secondA = []
    secondA.append(inp.readline().strip().split(' '))
    secondA.append(inp.readline().strip().split(' '))
    secondA.append(inp.readline().strip().split(' '))
    secondA.append(inp.readline().strip().split(' '))

    rowA = firstA[first - 1] 
    rowB = secondA[second - 1]

    inter = set(rowA).intersection(set(rowB))

    if len(inter) == 0:
        result = CHEATED
    elif len(inter) > 1:
        result = BAD
    else:
        result = inter.pop()

    outLine= "Case #" + str(i+1) + ": " + str(result)
    out.write(outLine + "\n")

    i = i + 1

inp.close()
out.close()

