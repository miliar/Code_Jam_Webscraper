import sys

def processCase():
    rowCounts, colCounts, diagCounts = [[0,0],[0,0],[0,0],[0,0]], [[0,0],[0,0],[0,0],[0,0]], [[0,0],[0,0]]
    hasDot = False
    for r in range(4):
        row = sys.stdin.readline()
        
        for c in range(4):
            if row[c] == 'X' or row[c] == 'T':
                rowCounts[r][0] += 1
                colCounts[c][0] += 1
                if r == c:
                    diagCounts[0][0] += 1
                elif r == 3 - c:
                    diagCounts[1][0] += 1
            if row[c] == 'O' or row[c] == 'T':
                rowCounts[r][1] += 1
                colCounts[c][1] += 1
                if r == c:
                    diagCounts[0][1] += 1
                elif r == 3 - c:
                    diagCounts[1][1] += 1
            if row[c] == '.':
                hasDot = True

    # read empty line
    sys.stdin.readline()
                
    for i in range(4):
        if rowCounts[i][0] == 4 or colCounts[i][0] == 4:
            return 'X won'
        elif rowCounts[i][1] == 4 or colCounts[i][1] == 4:
            return 'O won'
    for i in range(2):
        if diagCounts[i][0] == 4:
            return 'X won'
        elif diagCounts[i][1] == 4:
            return 'O won'
    if not hasDot:
        return 'Draw'
    else:
        return 'Game has not completed'

def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        result = processCase()
        print 'Case #%d: %s' % (i + 1, result)
        
if __name__ == '__main__':
    main()
