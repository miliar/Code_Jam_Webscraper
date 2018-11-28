import sys

def addItem(l, item):

    if l[-1][0] == item[0]:
        l[-1] = (item[0], l[-1][1] + item[1])
    else:
        l.append(item)
    return l

def solve(nstall, npeople):
    spaces = [(nstall, 1)]
    nNewSpaces = 1
    nSpaceSize = spaces[0][0]
    nNewSpaces = spaces[0][1]
    
    while npeople > nNewSpaces:
        if (nSpaceSize-1) % 2 == 0:
            new = (nSpaceSize-1)/2
            item = (new, nNewSpaces*2)
            spaces = addItem(spaces, item)
        else:
            othernew = (nSpaceSize-1)/2+1
            item = (othernew, nNewSpaces)
            spaces = addItem(spaces, item)
            new = (nSpaceSize-1)/2
            item = (new, nNewSpaces)
            spaces = addItem(spaces, item)
        
        npeople -= nNewSpaces
        spaces = spaces[1:]
        nSpaceSize = spaces[0][0]
        nNewSpaces = spaces[0][1]

    if ((nSpaceSize-1)%2 == 0):
        return str((nSpaceSize-1)/2) + " " + str((nSpaceSize-1)/2)
    else:
        return str(1+(nSpaceSize-1)/2) + " " + str((nSpaceSize-1)/2)



def process(filenamein):
    f = open(filenamein, "r")
    size = int(f.readline())
    for line in xrange(size):
        s = f.readline()
        l = s.split(" ")
        res = solve(int(l[0]), int(l[1]))
        out = "Case #" + str(line+1) + ": " + res
        print out
    f.close()

if len(sys.argv) == 2:
    process(sys.argv[1])