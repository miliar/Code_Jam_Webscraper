from sys import argv

script, filename = argv

f = open(filename)

T = int(f.readline())


def isEqual(a, b, t):
    if a != t and b != t:
        return False
    return a == 'T' or b == 'T' or a == b


def check(array):
    isUnfinished = False
    res = [[[0]*6 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            if array[i][j] == '.':
                isUnfinished = True
            else:
                a = array[i][j]
                if i == 0 and j == 0:
                    if a == 'T' or a == 'X':
                        res[0][0][0] = 1
                        res[0][0][1] = 1
                        res[0][0][2] = 1
                    if a == 'T' or a == 'O':
                        res[0][0][3] = 1
                        res[0][0][4] = 1
                        res[0][0][5] = 1
                elif i == 0:
                    if a == 'T' or a == 'X':
                        res[i][j][0] = 1
                        res[i][j][1] = res[i][j - 1][1] + 1
                        res[i][j][2] = 1
                    if a == 'T' or a == 'O':
                        res[i][j][3] = 1
                        res[i][j][4] = res[i][j - 1][4] + 1
                        res[i][j][5] = 1
                elif j == 0:
                    if a == 'T' or a == 'X':
                        res[i][j][0] = res[i - 1][j][0] + 1
                        res[i][j][1] = 1
                        if i + j == 3:
                            res[i][j][2] = res[i - 1][j + 1][2] + 1
                        else:
                            res[i][j][2] = 1
                    if a == 'T' or a == 'O':
                        res[i][j][3] = res[i - 1][j][3] + 1
                        res[i][j][4] = 1
                        if i + j == 3:
                            res[i][j][5] = res[i - 1][j + 1][5] + 1
                        else:
                            res[i][j][5] = 1
                else:
                    if a == 'T' or a == 'X':
                        res[i][j][0] = res[i - 1][j][0] + 1
                        res[i][j][1] = res[i][j - 1][1] + 1
                        if i == j:
                            res[i][j][2] = res[i - 1][j - 1][2] + 1
                        elif i + j == 3:
                            res[i][j][2] = res[i - 1][j + 1][2] + 1
                    if a == 'T' or a == 'O':
                        res[i][j][3] = res[i - 1][j][3] + 1
                        res[i][j][4] = res[i][j - 1][4] + 1
                        if i == j:
                            res[i][j][5] = res[i - 1][j - 1][5] + 1
                        elif i + j == 3:
                            res[i][j][5] = res[i - 1][j + 1][5] + 1
            if res[i][j][0] == 4 or res[i][j][1] == 4 or res[i][j][2] == 4:
                return 'X won'
            if res[i][j][3] == 4 or res[i][j][4] == 4 or res[i][j][5] == 4:
                return 'O won'
            #print res
    if isUnfinished:
        return 'Game has not completed'
    else:
        return 'Draw'


for t in range(T):
    array = ['', '', '', '']
    for j in range(4):
        array[j] = f.readline()

    print 'Case #{0}: {1}'.format(t + 1, check(array))
    f.readline()


f.close()
