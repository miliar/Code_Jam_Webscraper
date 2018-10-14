def readAt(file, i):
    fp = open(file, "r")
    
    for x in range(i):
        fp.readline()
    return fp.readline()
    
    fp.close()
    
def consecutive(line, start, stop, sad):
    for i in range(start, stop + 1):
        if ((line[i] != "-" and sad) or (line[i] != "+" and not sad)):
            return False
    return True

def flip(enter, start, stop):
    line = list(enter)
    for i in range(start, stop + 1):
        if (line[i] == "-"):
            line[i] = "+"
        else:
            line[i] = "-"
    return "".join(line)

filee = "testfile.txt"

testCases = int(readAt(filee, 0))

problems = []
minFlips = []

for i in range(1, testCases + 1):
    problems.append( readAt(filee, i).split(" "))
    minFlips.append(0)

for i in range(len(problems)):
    spatSize = int(problems[1])
    #start by flipping all obvious sads
    for x in range(len( problems[i][0] )): #iterate through characters in problems
        if (x + spatSize >= len(problems[i][0] )): #dont look past the end
            if ( consecutive(problems[i], x, x + spatSize, True) ): # if there is a line of sads
                minFlips[i] += 1
                problems[i][0]