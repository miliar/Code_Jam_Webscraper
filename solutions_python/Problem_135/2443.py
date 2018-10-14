# Google Codejam - Magic Trick

def CompareRows(FirstAnswer, FirstField, SecondAnswer, SecondField):
    FirstRow = FirstField[FirstAnswer - 1].split(' ')
    FirstRow = [int(z) for z in FirstRow]
    SecondRow = SecondField[SecondAnswer - 1].split(' ')
    SecondRow = [int(z) for z in SecondRow]
    CommonNumbers = []
    for i in FirstRow:
        if i in SecondRow:
            CommonNumbers.append(i)
    if len(CommonNumbers) == 0:
        return 'Volunteer cheated!'
    elif len(CommonNumbers) > 1:
        return 'Bad magician!'
    else:
        return CommonNumbers[0]

def main():
    try:
        f = open('magic.in','r')
    except:
        print('cannot open input file!')
    T = int(f.readline())
    for t in range(1, T + 1):
        print('Case #', t, ': ', end='', sep='')
        FirstAnswer = int(f.readline())
        FirstField = []
        for i in range(4):
            FirstField.append(f.readline())
        SecondAnswer = int(f.readline())
        SecondField = []
        for i in range(4):
            SecondField.append(f.readline())
        print(CompareRows(FirstAnswer, FirstField, SecondAnswer, SecondField))
    f.close()
    return 0

if __name__=='__main__':
    main()
