__author__ = 'abu-abdurahman'
contents = [list.strip() for list in open('A-small-attempt0.in') ]
numberOfInput = int(contents[0])


def getSolution(x, xList, y, yList):
    row1 = set(xList[x - 1])
    row2 = set(yList[y - 1])
    sol = row1 & row2
    if(len(sol) == 1):
        return sol.pop()
    elif(len(sol) > 1):
        return 'Bad magician!'
    else:
        return 'Volunteer cheated!'

#credit = []
j = 1
solution = []
for i in range(numberOfInput):
    firstAnswer = int(contents[j])
    j += 1
    firstArrangement = []
    for num in range(4):
        firstArrangement.append([int(x) for x in contents[j].split()])
        j += 1
    secondAnswer = int(contents[j])
    j += 1
    secondArrangement = []
    for num2 in range(4):
        secondArrangement.append([int(x) for x in contents[j].split()])
        j += 1
    solution.append(getSolution(firstAnswer, firstArrangement, secondAnswer, secondArrangement))


output = open('output.txt', 'w')
#output.write('Output \n')
for i in range(1, len(solution) + 1):
    output.write(str('Case #') + str(i) + ': ' + str(solution[i-1]) + '\n' )