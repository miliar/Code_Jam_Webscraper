# https://code.google.com/codejam/contest/2974486/

def readGrid(fp, rowNum):
    for i in range(1, 5):
        line = fp.readline()
        if i == rowNum:
            row = line.strip().split(' ')
    return set(row)

def solveCase():
    row1 = readGrid(fp, int(fp.readline()))
    row2 = readGrid(fp, int(fp.readline()))
    d = row1 & row2
    if len(d) == 0:
        return 'Volunteer cheated!'
    elif len(d) == 1:
        return list(d)[0]
    else:
        return 'Bad magician!'
    
if __name__ == '__main__':
    fp = open('A-small-attempt0.in')
    ap = open('answer.txt', 'w')
    tests = int(fp.readline())
    for i in range(tests):
        msg = "Case #%d: %s\n" % (i+1, solveCase())
        ap.write(msg)
        
    fp.close()
    ap.close()
