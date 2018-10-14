def printCase(case):
    for l in case:
        print(l)
    
def solveCase(case):
    possible = True

    h = len(case)
    for i in range(0, h):
        w = len(case[i])
        for j in range(0, w):
            x = case[i][j]

            # possible horisontal
            canHor = True
            for j2 in range(0, w):
                if case[i][j2] > x:
                    canHor = False
                    break

            # possible horisontal
            canVert = True
            for i2 in range(0, h):
                if case[i2][j] > x:
                    canVert = False
                    break

            can = canVert or canHor
            if not can:
                return 'NO'
        
    return 'YES'

def solve(sourceFile, resultFile):
    s = open(sourceFile)
    r = open(resultFile, 'w')

    count = int(s.readline())
    for n in range(1, count + 1):
        h, w = map(int, s.readline().split())
        case = []
        for j in range(0, h):
            string = s.readline()
            line = [int(i) for i in string.split()]
            case.append(line)
        
        # printCase(case)
        header = 'Case #' + str(n) + ': '
        r.write(header + solveCase(case) + '\n')
    return
        
def main():
    source = 'B-large.in'
    result = source + '.result.txt'
    solve(source, result)
    return

if __name__ == '__main__':
    main()
