def increase(spaces, space):
    for i in range(len(spaces)):
        if spaces[i][0] == space:
            spaces[i][1] += 1
            break
        elif spaces[i][0] > space:
            spaces.insert(i, [space, 1])
            break

def runStalls(numStalls, numPeople):
    spaces = [[numStalls, 1]]
    for i in range(numPeople):
        maxSpace = spaces[-1][0]
        half = (maxSpace - 1) // 2
        newSpaces = [half + (maxSpace + 1) % 2, half]
        for space in newSpaces:
            increase(spaces, space)
        spaces[-1][1] -= 1
        if spaces[-1][1] == 0:
            spaces.pop()
    return newSpaces

with open("input.in") as finput, open("output.out", "w") as foutput:
    numCases = int(finput.readline().strip())
    for i in range(1, numCases + 1):
        numStalls, numPeople = map(int, finput.readline().strip().split())
        answer = list(map(str, runStalls(numStalls, numPeople)))
        foutput.write("Case #" + str(i) + ": " + answer[0] + " " + answer[1] + "\n")
