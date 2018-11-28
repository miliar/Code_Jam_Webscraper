f = open('A-small-attempt1.in')
fo = open('A.txt', 'w')
for z in range(int(f.readline().strip())):
    g = []
    for i in range(4):
        g.append(list(f.readline().strip()))
    f.readline()
    inc = False
    msg = ''
    for i in range(4):
        for j in range(4):
            a = g[i][j]
            if a == '.': inc = True
            if i == 0 and j == 0 and not a == '.':
                for k in range(4):
                    if not (g[i+k][j+k] == a or g[i+k][j+k] == 'T'):
                        if g[i+k][j+k] == '.': inc = True
                        break
                else: msg = a + ' won'
            elif i == 0 and j == 3 and not a == '.':
                for k in range(4):
                    if not (g[i+k][j-k] == a or g[i+k][j-k] == 'T'):
                        if g[i+k][j-k] == '.': inc = True
                        break
                else: msg = a + ' won'

            if i == 0 and not a == '.':
                for k in range(4):
                    if not (g[i+k][j] == a or g[i+k][j] == 'T'):
                        if g[i+k][j] == '.': inc = True
                        break
                else: msg = a + ' won'

            if j == 0 and not a == '.':
                for k in range(4):
                    for k in range(4):
                        if not (g[i][j+k] == a or g[i][j+k] == 'T'):
                            if g[i][j+k] == '.': inc = True
                            break
                    else: msg = a + ' won'
            if not msg == '': break
        if not msg == '': break
    fo.write('Case #%d: ' %(z+1))
    if msg == '':
        if inc: fo.write('Game has not completed\n')
        else: fo.write ('Draw\n')
    else: fo.write(msg + '\n')
f.close()
fo.close()
