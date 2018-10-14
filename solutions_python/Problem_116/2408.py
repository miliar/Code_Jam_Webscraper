__author__ = 'mshafer'

def checkWin(combos, i):
    dot_found = False

    for combo in combos:
        if '.' not in combo:
            if 'O' not in combo:
                print "Case #" + str(i) + ": X won"
                return
            if 'X' not in combo:
                print "Case #" + str(i) + ": O won"
                return
        else:
            dot_found = True

    if dot_found:
        print "Case #" + str(i) + ": Game has not completed"
    else:
        print "Case #" + str(i) + ": Draw"



def main():
    f = file("A-large.in", "r")
    num_test_cases = int(f.readline())

    #Each test case
    for i in range(num_test_cases):
        #Extract rows
        combos = [None] * 10
        for j in range(5):
            if j != 4:
                combos[j] = list(f.readline().strip())
            else:
                f.readline()

        #Extract columns
        for j in range(4,8):
            combos[j] = [row[j - 4] for row in combos[0:4]]

        #Extract diagonals
        combos[8] = [row[y] for y, row in enumerate(combos[0:4])]
        combos[9] = [row[-y-1] for y, row in enumerate(combos[0:4])]

        checkWin(combos, i + 1)


if __name__ == '__main__':
    main()