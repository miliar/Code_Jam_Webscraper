import sys

def find4inarow(matrix, player):
    for y in xrange(4):
        # check horizontal
        for x in xrange(4):
            if not matrix[y][x] in ['T', player]:
                break
            elif x == 3:
                return True

        # check vertical
        for x in xrange(4):
            if not matrix[x][y] in ['T', player]:
                break
            elif x == 3:
                return True

    # check diagonals
    for xy in xrange(4):
        if not matrix[xy][xy] in ['T', player]:
            break
        elif xy == 3:
            return True

    for y in xrange(4):
        if not matrix[3-y][y] in ['T', player]:
            break
        elif y == 3:
            return True


    return False

def getresult(matrix):
    x = find4inarow(matrix, 'X')
    o = find4inarow(matrix, 'O')
    if x:
        return 'X won'
    elif o:
        return 'O won'
    else:
        #check for empty fields
        for x in xrange(4):
            if '.' in matrix[x]:
                return 'Game has not completed'
        return 'Draw'


if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    # d = {'O':0, 'B':1}
    for _t in xrange(t):
        mat = []
        for i in xrange(4):
            l = f.readline().rstrip()
            mat.append(l)

        f.readline()
        
        res = getresult(mat)
        print "Case #%d: %s" % (_t+1, res)

