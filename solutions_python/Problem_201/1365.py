import math

def findSolution(toilets, visitors):
    depth = 0
    if visitors > 1:
        depth = math.floor(math.log(visitors, 2))
    leafs = math.pow(2, depth)
    maxNumber = math.floor(toilets/leafs)
    highOptions = 0
    if visitors == 1:
        highOptions = 1
    else:
        highOptions = leafs - (leafs * maxNumber - (toilets - visitors + 1))
    choice = maxNumber - 1
    if highOptions > 0:
        choice = maxNumber
    if choice % 2 == 0:
        return str(int(choice/2)) + " " + str(int(choice/2 - 1))
    return str(math.floor(choice/2)) + " " + str(math.floor(choice / 2))

inp = open("C-small-2-attempt0.in", "r")
res = open("out1.txt", "w")
cases = int(inp.readline())
lines = []
for i in range(cases):
    lines.append(inp.readline())
for i in range(len(lines)):
    x, y = list(map(int,lines[i].rstrip().split()))
    res.write("Case #" + str(i+1) + ": " + findSolution(x, y) + "\n")
    print(i)