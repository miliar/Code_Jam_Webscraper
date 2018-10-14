# python 3.4 !!

#from functools import lru_cache
#@lru_cache(maxsize = None)

num_trials = int(input())

def isBlank(line):
    l = len(line)
    for i in range(0, l):
        if line[i] != '?':
            return False
    return True

def fillLine(line): # line must not be blank
    l = len(line)
    currChar = '.' # none
    haveEncountedFirstChar = False
    for i in range(0, l):
        if line[i] != '?':
            currChar = line[i]
            if not haveEncountedFirstChar:
                for j in range(0,i):
                    line = line[:j] + currChar + line[(j+1):]
                haveEncountedFirstChar = True
        else:
            if haveEncountedFirstChar:
                line = line[:i] + currChar + line[(i+1):]
    return line

def compute():
    R, C = map(int, input().split())

    lines = [""] * R
    for i in range(0, R):
        lines[i] = input()

    i = 0
    while isBlank(lines[i]): # guaranteed to fail before out of bound
        i += 1 

    blankLinesTop = i
    lines[i] = fillLine(lines[i])
    for j in range(0, i):
        lines[j] = lines[i]
    currLine = lines[i]

    for j in range(i+1,R):
        if isBlank(lines[j]):
            lines[j] = currLine
        else:
            lines[j] = fillLine(lines[j])
            currLine = lines[j]

    str = ""
    for j in range(0, R):
        str += "\n"
        str += lines[j]

    return str

for i in range (0, num_trials):
    print("Case #" + str(i+1) + ": " + compute())
