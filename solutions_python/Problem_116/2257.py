
def column(matrix, i):
    return [row[i] for row in matrix]

def processBoard(b):
    #print(b)

    dotFound = False
    for row in b:
        x = row.count('X')
        o = row.count('O')
        t = row.count('T')
        d = row.count('.')

        if x == 4 or (x == 3 and t == 1):
            return "X won"
        if o == 4 or (o == 3 and t == 1):
            return "O won"
        if d > 0:
            dotFound = True

    for i in range(0, 4):
        col = column(b, i)
        #print(col)
        
        x = col.count('X')
        o = col.count('O')
        t = col.count('T')
        d = col.count('.')

        if x == 4 or (x == 3 and t == 1):
            return "X won"
        if o == 4 or (o == 3 and t == 1):
            return "O won"
        if d > 0:
            dotFound = True

    dl = []
    dr = []
    for i in range(0, 4):
        dl.append(b[i][i])
        dr.append(b[-i-1][i])

    x = dl.count('X')
    o = dl.count('O')
    t = dl.count('T')
    d = dl.count('.')

    if x == 4 or (x == 3 and t == 1):
        return "X won"
    if o == 4 or (o == 3 and t == 1):
        return "O won"
    if d > 0:
        dotFound = True

    x = dr.count('X')
    o = dr.count('O')
    t = dr.count('T')
    d = dr.count('.')

    if x == 4 or (x == 3 and t == 1):
        return "X won"
    if o == 4 or (o == 3 and t == 1):
        return "O won"
    if d > 0:
        dotFound = True

    if dotFound:
        return "Game has not completed"
    else:
        return "Draw"


def main():
    filePath = "input/A-large.in"
    file = open(str(filePath))
    
    lines = [line.strip() for line in file]
    lines = list(filter(lambda s: s != "", lines))

    T = int(lines[0])
    lines = lines[1:]

    for t in range(0, T):
        b = []
        b.append(lines[4*t])
        b.append(lines[4*t+1])
        b.append(lines[4*t+2])
        b.append(lines[4*t+3])
        output = processBoard(b)
        print("Case #%s: %s" % (t+1, output))










main()
