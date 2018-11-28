def checkCompl(field):
    for i in field:
        for j in i:
            if j == '.':
                return True
    return False


def checkWin(poss, s):
    solution = s*4
    res = []
    for i in poss:
        st = ""
        for j in i:
            if j == "T":
                st = st + s
            else:
                st = st + j
        res.append(st)
    print ''
    print poss
    print res
    for i in res:
        if solution == i:
            return True
    return False


def checkField(field):
    cols = []
    d1 = ""
    d2 = ""
    for i in range(4):
            l = ""
            for j in range(4):
                l = l + field[j][i]
                if i == j:
                    d1 = d1 + field[j][i]
                if i == 3 - j:
                    d2 = d2 + field[j][i]
            cols.append(l)
    poss = cols + field
    poss.append(d1)
    poss.append(d2)
    if checkWin(poss, 'X'):
        return "X won"
    if checkWin(poss, 'O'):
        return "O won"
    if checkCompl(field):
        return "Game has not completed"
    return "Draw"


def main():
    txtin = open("input.txt", "r")
    txtout = open("output.txt", "w")
    cases = int(txtin.readline())
    writelines = []
    for case in range(1, cases+1):
        field = []
        for j in range(4):
            field.append(txtin.readline()[:-1])
        txtin.readline()
        res = "Case #" + str(case) + ": " + checkField(field) + '\n'
        writelines.append(res)
    txtout.writelines(writelines)
    txtout.close()

if __name__ == '__main__':
    main()
