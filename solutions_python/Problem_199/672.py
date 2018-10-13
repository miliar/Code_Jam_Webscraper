
def readInput(path):
    cases = []
    with open(path, mode='r') as f:
        numCases = f.readline().strip()
        for line in f:
            split = line.strip().split(" ")
            numPancakes = int(split[1])
            pancakeString = split[0]
            trueList = [i == '-' for i in pancakeString]
            cases.append((numPancakes, trueList))

    return numCases, cases

def flipPancake (pancakes, position, size):
    before = pancakes[:(position)]
    flip = pancakes[position:(position+size)]
    after = pancakes[(position+size):]
    flip = [not i for i in flip]

    return before+flip+after

def countFlips (pancakes, size):
    flips=0
    for i in range(len(pancakes)-size+1):
        if pancakes[i]:
            pancakes=flipPancake(pancakes, i, size)
            flips+=1

    if set(pancakes)=={False}:
        return(str(flips))
    else:
        return("IMPOSSIBLE")

def printSolutions(solutions):
    with open("Output", mode='w') as f:
        case = 0
        for solution in solutions:
            case+=1
            f.writelines("Case #"+str(case)+": "+solution+"\n")



numcases, data = readInput("Input")
solutions = []
for size, pancakes in data:
    solutions.append(countFlips(pancakes,size))

printSolutions(solutions)
