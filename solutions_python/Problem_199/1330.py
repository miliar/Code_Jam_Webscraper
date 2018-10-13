def findSolution(pancakes, flipper):
    total = len(pancakes)
    flips = 0
    
    for i in range(total):
        if pancakes[i] == '-':
            if total - i < flipper:
                return "IMPOSSIBLE"
            else:
                flips += 1
                for j in range(i, i + flipper):
                    if pancakes[j] == '+':
                        pancakes[j] = '-'
                    else:
                        pancakes[j] = '+'
    return str(flips)

inp = open("A-large.in", "r")
res = open("out1.txt", "w")
cases = int(inp.readline())
lines = []
for i in range(cases):
    lines.append(inp.readline())
for i in range(len(lines)):
    pancakes, flipperSize = lines[i].rstrip().split(" ");
    res.write("Case #" + str(i+1) + ": " + findSolution(list(pancakes), int(flipperSize)) + "\n")
    print(i)