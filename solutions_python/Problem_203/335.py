inputF = open('A-large.in', 'r')
output = open('A-large.out', 'w')

def makeCakeString(startingCakeLines):
    ''' Makes a cake string, given the lines (rows) to start with as a
        list of strings '''
    emptyStartLines = 0
    lines = []
    for line in startingCakeLines:
        newLine = ''
        firstChar = ''
        for c in line:
            if c != '?':
                firstChar = c
                break
        if firstChar == '':
            if len(lines) == 0:
                emptyStartLines += 1
            else:
                lines = lines + [lines[-1]]
            continue
        for c in line:
            if c != '?' and c != firstChar:
                firstChar = c
            newLine = newLine + firstChar
        lines += [newLine]
    s = (lines[0]+'\n')*emptyStartLines
    for line in lines:
        s += line + '\n'
    return s
    
        


numCases = int(inputF.readline())

for i in range(numCases):
    r, c = inputF.readline().split()
    lines = []
    for j in range(int(r)):
        lines += [inputF.readline().strip()]
    cakeStr = makeCakeString(lines)

    output.write('Case #' + str(i+1) + ': \n')
    output.write(cakeStr)

inputF.close()
output.close()

