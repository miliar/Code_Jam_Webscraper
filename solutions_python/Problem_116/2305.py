#code jam Tic Tac Tomek

def Tic_Tac_Tomek(filepath):
    inputfile = open(filepath)
    num_case = int(inputfile.readline())
    for i in range(num_case):
        l1 = inputfile.readline()
        l2 = inputfile.readline()
        l3 = inputfile.readline()
        l4 = inputfile.readline()
        buf = inputfile.readline()
        ans = solve_TTT(l1,l2,l3,l4)
        print("Case #" + str(i+1) + ": " + ans)

def solve_TTT(l1,l2,l3,l4):
    colx = [0,0,0,0]
    coly = [0,0,0,0]
    rowx = [num(l1,'X'),num(l2,'X'),num(l3,'X'),num(l4,'X')]
    rowy = [num(l1,'O'),num(l2,'O'),num(l3,'O'),num(l4,'O')]
    diagx = [0,0]
    diagy = [0,0]
    for i in range(4):
        colx[i] = iss(l1[i],'X') + iss(l2[i],'X') + iss(l3[i],'X') + iss(l4[i],'X')
        coly[i] = iss(l1[i],'O') + iss(l2[i],'O') + iss(l3[i],'O') + iss(l4[i],'O')
    diagx[0] = iss(l1[0],'X') + iss(l2[1],'X') + iss(l3[2],'X') + iss(l4[3],'X')
    diagy[0] = iss(l1[0],'O') + iss(l2[1],'O') + iss(l3[2],'O') + iss(l4[3],'O')
    diagx[1] = iss(l4[0],'X') + iss(l3[1],'X') + iss(l2[2],'X') + iss(l1[3],'X')
    diagy[1] = iss(l4[0],'O') + iss(l3[1],'O') + iss(l2[2],'O') + iss(l1[3],'O')
    if max([max(diagx),max(rowx),max(colx)]) == 4:
        return "X won"
    if max([max(diagy),max(rowy),max(coly)]) == 4:
        return "O won"
    if total_char(l1,l2,l3,l4) < 16:
        return "Game has not completed"
    return "Draw"


def iss(ch1,ch2):
    if ch1==ch2 or ch1 == 'T':
        return 1
    else:
        return 0

def num(l,ch):
    ans = 0
    for i in range(len(l)):
        if l[i] == ch or l[i] == 'T':
            ans = ans + 1
    return ans

def total_char(l1,l2,l3,l4):
    t = 0
    for i in range(4):
        if l1[i] != '.':
            t = t + 1
        if l2[i] != '.':
            t = t + 1
        if l3[i] != '.':
            t = t + 1
        if l4[i] != '.':
            t = t + 1
    return t
