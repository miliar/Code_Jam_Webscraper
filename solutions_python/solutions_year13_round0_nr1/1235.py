listOfChecks = [[ 0,  1,  2,  3],
                [ 4,  5,  6,  7],
                [ 8,  9, 10, 11],
                [12, 13, 14, 15],
                [ 0,  4,  8, 12],
                [ 1,  5,  9, 13],
                [ 2,  6, 10, 14],
                [ 3,  7, 11, 15],
                [ 0,  5, 10, 15],
                [ 3,  6,  9, 12]]

def getState(f):
    state = ''
    for x in range(5):
        state += f.readline()[:-1]
    return state

def checkState(state):
    for check in listOfChecks:
        checkState = ''
        for index in check:
            checkState += state[index]
        if '.' in checkState:
            continue
        else:
            if 'X' in checkState and 'O' not in checkState:
                return 'X won'
            elif 'O' in checkState and 'X' not in checkState:
                return 'O won'
    if '.' in state:
        return 'Game has not completed'
    else:
        return 'Draw'



if __name__ == '__main__':
    fileIn = open('A-large.in', 'r')
    fileOut = open('A-large-output.out', 'w')

    testCases = int(fileIn.readline()[:-1])

    for case in range(1,testCases+1):
        output = 'Case #%r: ' % (case) + checkState(getState(fileIn)) + '\n'
        fileOut.write(output)

    fileIn.close()
    fileOut.close()
