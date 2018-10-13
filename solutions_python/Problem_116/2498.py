import sys

def getlist(s):
    return [x for x in list(s) if x!='\n']

def makebox(fd):
    box = []
    for i in range(0,4):
        row = getlist(fd.readline())
        box.append(row)
    return box

def didwin(letter, b):
    for i in range(0,4):
        count = 0
        for j in range(0,4):
            ind = b[i][j]
            if ind == letter:
                count += 1
            elif ind == 'T':
                if count == 0:
                    count += 1
                elif count == 3:
                    return 1
                else:
                    break
            else:
                break
        if count == 4:
            return 1

    for i in range(0,4):
        count = 0
        for j in range(0,4):
            ind = b[j][i]
            if ind == letter:
                count += 1
            elif ind == 'T':
                if count == 0:
                    count += 1
                elif count == 3:
                    return 1
                else:
                    break
            else:
                break
        if count == 4:
            return 1

    count = 0
    for i in range(0,4):
        ind = b[i][i]
        if ind == letter:
            count += 1
        elif ind == 'T':
            if count == 0:
                count += 1
            elif count == 3:
                return 1
            else:
                break
        else:
            break
        if count == 4:
            return 1
        
    count = 0
    for i in range(0,4):
        ind = b[i][3-i]
        if ind == letter:
            count += 1
        elif ind == 'T':
            if count == 0:
                count += 1
            elif count == 3:
                return 1
            else:
                break
        else:
            break
        if count == 4:
            return 1

    return 0

def drawgame(b):
    for i in range(0,3):
        for j in range(0,3):
            if b[i][j] == '.':
                return 0
    return 1

def case(fd):
    b = makebox(fd)
    fd.readline()

    if didwin('O',b):
        return 'O won'
    if didwin('X',b):
        return 'X won'
    if drawgame(b):
        return 'Draw'
    else:
        return 'Game has not completed'

    return 'testing'

def main():
    fd = sys.stdin
    n = int(fd.readline())
    for i in range(n):
        print 'Case #%d: %s' % (i+1, case(fd))

main()

