def fl():
    l = fi.readline()
    return l[:4]

def check(s):
    o = 0
    x = 0
    emp = False
    ove = False
    for i in range(4):
        if s[i] == 'O':
            o = o + 1
        elif s[i] == 'X':
            x = x + 1
        elif s[i] == 'T':
            x = x + 1
            o = o + 1
        elif s[i] == '.':
            emp = True

    if o == 4:
        ove = True
        fo.write("O won\n")
    elif x == 4:
        ove = True
        fo.write("X won\n")
    return ove, emp

fi = open("input.in",'r')
fo = open("output.out", 'w')

t = int(fi.readline()[:-1])

for i in range(t):
    fo.write("Case #%s: " % (i+1))
    
    over = False
    empty = False
    mat = ['','','','','','']
    for j in range(4):
        l = fl()
        ##print(l)
        for p in range(4):
            mat[p] = mat[p] + l[p]
            if (j == p):
                mat[4] = mat[4] + l[p]
            if (j + p == 3):
                mat[5] = mat[5] + l[p]
        if (not over):
            over, empty = check(l)

    for j in range(6):
        if (not over):
            over, empty = check(mat[j])

    if (not over) and empty:
        fo.write("Game has not completed\n")
    if (not over) and (not empty):
        fo.write("Draw\n")

    l = fl()

fi.close()
fo.close()
