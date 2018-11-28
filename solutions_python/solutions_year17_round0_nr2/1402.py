def findSolution(number):
    if number == "0":
        return ""
    solution = ""
    nines = 0
    lowest = 0
    for charIndex in range(len(number)):
        if int(number[charIndex]) < lowest:
            nines = len(number)-charIndex
            break
        else:
            solution += number[charIndex]
            lowest = int(number[charIndex])
    
    #handle decrease
    if nines != 0:
        solution = str(int(solution) - 1)
        solution = findSolution(solution) + nines * '9'
        
    return solution

inp = open("B-large.in", "r")
res = open("out1.txt", "w")
cases = int(inp.readline())
lines = []
for i in range(cases):
    lines.append(inp.readline())
for i in range(len(lines)):
    res.write("Case #" + str(i+1) + ": " + findSolution(lines[i].rstrip()) + "\n")
    print(i)