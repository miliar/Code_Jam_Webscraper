from sys import stdout
fi = open('A-large.in','r')
fo = open('A-large.out','w')
n = int(fi.readline())
x = {'X','T'}
y = {'O','T'}
for t in range(n):
    k = 0
    l = [['.','.','.','.'],['.','.','.','.'],['.','.','.','.'],['.','.','.','.']]
    for i in range(4):
        st = fi.readline()
        for j in range(4):
            l[i][j] = st[j]
            if st[j] == '.':
                k = 1
    fi.readline()
    fo.write('Case #'+str(t+1)+str(': '))
    if l[0][0] in x and l[1][1] in x and l[2][2] in x and l[3][3] in x:
        fo.write('X won\n')
        continue
    if l[0][3] in x and l[1][2] in x and l[2][1] in x and l[3][0] in x:
        fo.write('X won\n')
        continue 
    if l[0][0] in y and l[1][1] in y and l[2][2] in y and l[3][3] in y:
        fo.write('O won\n')
        continue
    if l[0][3] in y and l[1][2] in y and l[2][1] in y and l[3][0] in y:
        fo.write('O won\n')
        continue
    
    for j in range(4):
        if l[j][0] in x and l[j][1] in x and l[j][2] in x and l[j][3] in x:
            k = 2
            break        
        if l[j][0] in y and l[j][1] in y and l[j][2] in y and l[j][3] in y:
            k = 3
            break
        if l[0][j] in x and l[1][j] in x and l[2][j] in x and l[3][j] in x:
            k = 2
            break        
        if l[0][j] in y and l[1][j] in y and l[2][j] in y and l[3][j] in y:
            k = 3
            break
    if (k == 2):
        fo.write('X won\n')
    elif (k == 3):
        fo.write('O won\n')
    elif (k == 1):
        fo.write('Game has not completed\n')
    else:
        fo.write('Draw\n')
fo.close()
fi.close()
