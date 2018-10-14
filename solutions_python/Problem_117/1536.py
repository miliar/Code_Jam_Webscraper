f = open('second.txt')
datas = f.read().split('\n')
f.close()

nb = int(datas[0])

pos = 1
final = ''
for k in range(nb):
    size = datas[pos]
    x = int(size.split()[0])
    y = int(size.split()[1])
    lawn = datas[pos + 1: pos + 1 + x]
    pos += x + 1

    for j in range(len(lawn)):
        lawn[j] = lawn[j].split()

    valid = True
    for xc in range(x):
        for yc in range(y):
            if xc > 0 and xc < x - 1 and yc > 0 and yc < y - 1:
                pass
            if True:
                current = lawn[xc][yc]
                firstOk = True
                secondOk = True
                for X in range(x):
                    if lawn[X][yc] > current:
                        firstOk = False
                for Y in range(y):
                    if lawn[xc][Y] > current:
                        secondOk = False
                if not firstOk and not secondOk:
                    valid = False
    if k == 16:
        print(valid, lawn)
    if valid:
        final += 'Case #'+str(k+1)+': YES\n'
    else:
        final += 'Case #'+str(k+1)+': NO\n'

print(final[:-1])
f = open('secondr.txt', 'w')
f.write(final)
f.close()
