# -*- coding: utf-8 -*-

data = open('A.in', 'r').read().split('\n')
output = open('A.out', 'w')

T = int(data.pop(0))
print data

for t in range(T):
    (R,C) = map(int, data.pop(0).split(' '))
    rows = []
    impossible = False
    for r in range(R):
        rows.append(list(data.pop(0)))
    #go from top to bottom, left to right, and replace in site
    for i in range(R-1):
        if not impossible:
            for j in range(C-1):
                if rows[i][j] == '#':
                    if rows[i+1][j] == '#' and rows[i+1][j+1] == '#' and rows[i][j+1] == '#':
                        rows[i][j] = '/'
                        rows[i+1][j] = '\\'
                        rows[i+1][j+1] = '/'
                        rows[i][j+1] = '\\'
                    else:
                        impossible = True
                        break
        else:
            break

    if not impossible and '#' in rows[R-1]:
        impossible = True
    for i in range(R):
        if not impossible:
            if rows[i][-1] == '#':
                impossible = True
        else:
            break

    if impossible:
        print 'Case #' + str(t+1) + ': Impossible'
        output.write('Case #' + str(t+1) + ':\nImpossible\n')
    else:
        print 'Case #' + str(t+1) + ':'
        output.write('Case #' + str(t+1) + ':\n')
        for row in rows:
            print ''.join(row)
            output.write(''.join(row) + '\n')
output.close()

