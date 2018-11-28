def readInput(path):
    cases = []
    with open(path, mode='r') as f:
        numCases = f.readline().strip()

        while True:
            line = f.readline().strip().split(' ')
            if line==['']:
                break

            cake = []
            rows = int(line[0])
            cols = int(line[1])

            for i in range(rows):
                cake.append(f.readline().strip())

            cases.append(cake)

    return numCases, cases


def printSolutions(solutions, name):
    with open(name, mode='w') as f:
        case = 0
        for solution in solutions:
            case+=1
            f.writelines("Case #"+str(case)+":\n")
            for row in solution:
                print(row)
                f.writelines(row + "\n")

numCases, cases = readInput("A-small-attempt0 (1).in")

def FillRow(above, current):
    new = ''
    for i in range(len(current)):
        if current[i] == '?':
            new += above[i]
        else:
            new += current[i]
    return new


def FillDown(cake, rows):
    above = cake[0]
    newCake = [above]
    for i in range(1,rows):
        newCake.append(FillRow(above, cake[i]))
        above = FillRow(above, cake[i])
    return newCake

def FillUp(cake, rows):
    cake = cake[::-1]
    cake = FillDown(cake, rows)
    return (cake[::-1])


def FillRight(cake, cols):
    cake = cake
    toprow = cake[0]
    if toprow[0]=='?':
        for i in range(len(cake)):
            cake[i] = cake[i][1]+cake[i][1:]

    for j in range(1,cols):
        if toprow[j]=='?':
            for i in range(len(cake)):
                cake[i] = cake[i][:j]+cake[i][j-1]+cake[i][j+1:]


    return cake

def FillLeft(cake, cols):
    newcake=[]
    for row in cake:
        newcake.append(row[::-1])
    FillRight(newcake, cols)
    solution=[]
    for row in newcake:
        solution.append(row[::-1])

    return solution


def FillCake(cake):
    rows = len(cake)
    cols = len(cake[0])
    cake = FillDown(cake, rows)
    cake = FillUp(cake, rows)
    cake = FillRight(cake, cols)
    cake = FillLeft(cake, cols)
    return cake

solution=[]
for cake in cases:
    solution.append(FillCake(cake))
printSolutions(solution, 'outputA')
