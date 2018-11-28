# -*- coding: utf-8 -*-

# ○×

#INPUT = 'A-small-attempt4.in'
#OUTPUT = 'output-a-small.txt'
INPUT = 'A-large.in'
OUTPUT = 'output-a-large.txt'

def check(caseno, data, isT, isDOT):
    isresult = False
    for idx in range(0, 4):
        row = data[idx]
        col = [data[i][idx] for i in range(0, 4)]
        # 対角線
        diagonal = []
        if idx == 0:
            diagonal = [data[j][j] for j in range(0, 4)]
        if idx == 3:
            diagonal = [data[j][3-j] for j in range(0, 4)]

        # チェック
        if row.count('X') == 4 or col.count('X') == 4 or (diagonal and diagonal.count('X') == 4):
            isresult = True
            result(caseno, 'X won')
            break

        if row.count('O') == 4 or col.count('O') == 4 or (diagonal and diagonal.count('O') == 4):
            isresult = True
            result(caseno, 'O won')
            break

        if 'T' in row:
            if row.count('X') == 3:
                isresult = True
                result(caseno, 'X won')
                break
            if row.count('O') == 3:
                isresult = True
                result(caseno, 'O won')
                break

        if 'T' in col:
            if col.count('X') == 3:
                isresult = True
                result(caseno, 'X won')
                break
            if col.count('O') == 3:
                isresult = True
                result(caseno, 'O won')
                break

        if diagonal and 'T' in diagonal:
            if diagonal.count('X') == 3:
                isresult = True
                result(caseno, 'X won')
                break
            if diagonal.count('O') == 3:
                isresult = True
                result(caseno, 'O won')
                break

    if not isresult:
        if isDOT:
            result(caseno, 'Game has not completed')
        else:
            result(caseno, 'Draw')

def result(caseno, msg):
    output = open(OUTPUT, 'a')
    output.write('Case #%d: %s\n' % (caseno, msg))
    output.close()

def main():
    input = open(INPUT, 'r')

    caseno = 0
    isT = False
    isDOT = False
    data = []
    input.readline()    # 1行目は無視
    for line in input:
        line = line.replace('\n', '')
        if not line:
            caseno += 1
            check(caseno, data, isT, isDOT)
            isT = False
            isDOT = False
            data = []
            continue

        _data = list(line)
        if 'T' in _data:
            isT = True
        if '.' in _data:
            isDOT = True
        data.append(_data)

    if data:
        caseno += 1
        check(caseno, data, isT)

    input.close()


if __name__ == '__main__':
    main()
