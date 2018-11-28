import sys, string

def checkline(line):
    no = 0
    nx = 0
    nt = 0
    for el in line:
       if el == 'O': no += 1
       elif el == 'X': nx += 1
       elif el == 'T': nt += 1
    if nt + nx == 4: return 'X'
    elif nt + no == 4: return 'O'
    else: return None

def empty(line):
    n = 0
    for el in line:
        if el == '.': n += 1
    return n


def tictactoe(ttt):
    nempty = 0
    for row in ttt:
        res = checkline(row)
        nempty += empty(row)
        if res:
            if res == 'X': return 'X won'
            else: return 'O won'
    for col in zip(*ttt):
        res = checkline(col)
        if res:
            if res == 'X': return 'X won'
            else: return 'O won'
    diag1 = []
    diag2 = []
    n = 0
    m = 3
    for row in ttt:
#        print row, n, m
        diag1.append(row[n])
        diag2.append(row[m])
        n += 1
        m -= 1
    res = checkline(diag1)
    if res:
        if res == 'X': return 'X won'
        else: return 'O won'
    res = checkline(diag2)
    if res:
        if res == 'X': return 'X won'
        else: return 'O won'
    if nempty == 0: return 'Draw'
    return 'Game has not completed'

def main(args):
    f = file(args[1])
    ncases = int(f.readline())
    for i in range(ncases):
        ttt = []
        for n in range(4):
            line = f.readline().rstrip()
            ttt.append(line)
        f.readline()
        ans = tictactoe(ttt)
        sys.stdout.write("Case #%d: %s\n" % (i+1, ans))

if __name__ == "__main__":
    main(sys.argv)