def counting(pos):
    result = [pos / 4, pos % 4 + 4]
    if pos in [0,5,10,15]:
        result.append(8)
    if pos in [3,6,9,12]:
        result.append(9)
    return result
def process(board):
    finished = True
    resultX = [0 for x in range(10)]
    resultO = [0 for x in range(10)]
    xScore = {'X':1, 'O': 0, 'T':1, '.':0}
    yScore = {'X':0, 'O': 1, 'T':1, '.':0}
    for i, move in enumerate(board):
        temp = counting(i)
        if move == ".":
            finished = False
        for item in temp:
            resultX[item] += xScore[move]
            resultO[item] += yScore[move]
    if max(resultX) == 4:
        return "X"
    if max(resultO) == 4:
        return "O"
    if not finished:
        return "U"
    return "D"

def output (fo, result, no):
    prefix = "Case #" + str(no+1) + ": "
    print result
    if result == 'X':
        postfix = "X won\n"
    if result == 'O':
        postfix = "O won\n"
    if result == 'D':
        postfix = "Draw\n"
    if result == 'U':
        postfix = "Game has not completed\n"
    fo.write (prefix + postfix)
def input(fname, foname):
    f = open(fname)
    line = f.readline()
    line = line.strip()
    no = int(line)
    fo = open(foname, "w")
    for i in range(no):
        line1 = f.readline().strip()
        line2 = f.readline().strip()
        line3 = f.readline().strip()
        line4 = f.readline().strip()
        f.readline()
        line = line1 + line2 + line3 + line4
        output(fo, process(line), i)
    f.close()
    fo.close()

input ("input.in", "result")
