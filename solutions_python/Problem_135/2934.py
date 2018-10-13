import sys


def input_generator():
    for line in sys.stdin:
        for token in line[:-1].split(' '):
            if token != '' or token:
                yield token

myin = input_generator()

def magicTrick(row1, row2):
    inCommon = []
    for i in range(len(row1)):
        for j in range(len(row2)):
            if row1[i] == row2[j]:
                inCommon.append(row1[i])
    if len(inCommon) == 1:
        return str(inCommon[0])
    if len(inCommon) > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"

def getRow():
    answer = int(myin.next())
    cards = []
    for i in range(16):
        cards.append(int(myin.next()))
    row = []
    for i in range(4):
        row.append(cards[((answer-1)*4)+i])
    return row



if __name__ == '__main__':
    tests = int(myin.next())
    for t in range(tests):
        result = magicTrick(getRow(), getRow())
        print 'Case #' + str(t+1) + ': ' + result
