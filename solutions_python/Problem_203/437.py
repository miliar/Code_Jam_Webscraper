def f(lines):
    e0 = countEmtpyLines(lines, 0)
    n = e0
    
    newLines = []

    while n < len(lines):
        line = lines[n]
        e = countEmtpyLines(lines, n+1)

        newLine = genFilledLine(line)

        for i in range(e+e0+1):
            newLines.append(newLine)

        n += (e+1)
        e0 = 0

    return newLines

        
def genFilledLine(line):
    e0 = countEmptyChars(line, 0)
    n = e0

    newLine = ''

    while n < len(line):
        c = line[n]
        e = countEmptyChars(line, n+1)

        newLine += c*(e+e0+1)
        n += (e+1)
        e0 = 0

    return newLine
    

        
def countEmptyChars(line, colNo):
    if colNo >= len(line):
        return 0

    n = 0
    for c in line[colNo:]:
        if c != '?':
            break
        n += 1
    
    return n


def countEmtpyLines(lines, lineNo):
    if lineNo >= len(lines):
       return 0 

    n = 0

    for line in lines[lineNo:]:
        if not isEmptyLine(line):
            break
        n += 1
    
    return n


def isEmptyLine(line):
    for c in line:
        if c != '?':
            return False
    
    return True

t = int(input())
for testCase in range(1, t+1):
    r, c = map(int, input().split())
    lines = [input() for i in range(r)]

    print('Case #' + str(testCase) + ':')
    print("\n".join(f(lines)))

        
