import sys

bad = "Bad magician!"
cheat = "Volunteer cheated!"

def check(grid1, grid2, row1, row2):
    r1 = grid1[(row1-1)]
    r2 = grid2[(row2-1)]
    intersection = filter(lambda x: x in r2,r1)
    if len(intersection) == 1:
        return intersection[0]
    elif len(intersection) == 0:
        return cheat
    else:
        return bad


def checkLines(data):
    row1 = int(data[0])
    row2 = int(data[5])
    grid1 = map(lambda x: map(int, x.split(" ")), data[1:5])
    grid2 = map(lambda x: map(int, x.split(" ")), data[6:10])
    return check(grid1, grid2, row1, row2)

##parsing
def getData(fileName):
    f = open(fileName, 'r+')
    lines = [line for line in f]
    nCases = int(lines[0])
    lines = lines[1:]
    k = 1
    while k <= nCases:
        tmp = lines[0:10]
        lines = lines[10:]
        print "Case #"+str(k)+": "+str(checkLines(tmp))
        k = k+1


getData(sys.argv[1])
