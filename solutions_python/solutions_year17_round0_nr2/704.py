
def readInput(path):
    cases = []
    with open(path, mode='r') as f:
        numCases = f.readline().strip()
        for line in f:
            cases.append(line.strip())

    return numCases, cases

def printSolutions(solutions):
    with open("Output-BLarge", mode='w') as f:
        case = 0
        for solution in solutions:
            case+=1
            f.writelines("Case #"+str(case)+": "+solution+"\n")

def maxNumber(number):
    max=0
    location = 0
    current=-1
    for digit in number:
        current+=1
        if int(digit)>max:
            max=int(digit)
            location=current

    return (max,location)


def solve(number):
    numDigits = len(number)
    if numDigits==0:
        return ''

    if isTidy(number):
        return number

    for i in range(len(number)):
        revIndex = len(number)-1-i
        if int(number[revIndex])<int(number[revIndex-1]):
            break


    max, maxLocation = maxNumber(number[:revIndex])

    if max==1:
        return '9'*(numDigits-1)

    return solve(number[0:maxLocation] + str(max-1) + '9'*(numDigits-maxLocation-1))



def isTidy(number):
    prev = int(number[0])
    for i in range(len(number)):
        if int(number[i])<prev:
            return False
        else:
            prev = int(number[i])
    return True

def solve2(number):
    lastTidy=0
    for count in range(int(number)+1):
        if isTidy(str(count)):
            lastTidy = count
    return lastTidy


numcases, data = readInput("B-large.in")

solutions = []
for number in data:
    solutions.append(solve(number))


printSolutions(solutions)
