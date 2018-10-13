fin = open('A-small-attempt0.in', 'r')
fout = open('aAns.txt', 'w')

def isend(mas):
    for i in range(4):
        ans = allequal(mas[i])
        if ans[0]:
            return ans[1] + ' won'
    for i in range(4):
        ans = allequal(getcol(mas,i))
        if ans[0]:
            return ans[1] + ' won'
    diags = getdiags(mas)
    ans = allequal(diags[0])
    if ans[0]:
        return ans[1] + ' won' 
    ans = allequal(diags[1])
    if ans[0]:
        return ans[1] + ' won' 
    point = 0
    for i in range(4):
        if mas[i].count('.') != 0:
            point = 1
    if point:
        return 'Game has not completed'
    else:
        return 'Draw'
    return

def getdiags(mas):
    diag1 = [mas[n][n] for n in range(4)]
    diag2 = [mas[n][3-n] for n in range(4)]
    return [diag1, diag2]

def getcol(mas, n):
    ans = [i[n] for i in mas]
    return ans

def allequal(mas):
    if mas.count('.') != 0:
        return [0]
    if mas[0] != 'T':
        for i in range(4):
            if mas[i] == 'T':
                mas[i] = mas[0]
    else:
        for i in range(4):
            if mas[i] == 'T':
                mas[i] = mas[1]
    if mas[0] == mas[1] == mas[2] == mas[3]:
        return [1, mas[0]]
    else:
        return [0]

T = int(fin.readline())
for i in range(T):
    lines = [list(fin.readline().strip()) for j in range(4)]
    fin.readline()
    fout.write('Case #' + str(i + 1) + ': ' + isend(lines) + '\n')



fin.close()
fout.close()
