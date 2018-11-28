def dumb(ln):
    for i in ln:
        for j in range(3):
            b = i[j]
            k = j+1
            if (b == i[k]) or (i[k] == 'T') or (b == 'T'):
                if k == 3:
                    if b == 'T':
                        return i[k]
                    return b
                continue
            break
    return None

def check(ln):
    ln2 = ['', '', '', '']
    ln3 = ['', '']
    for i in range(4):
        for j in range(4):
            ln2[i] += ln[j][i]
    for i in range(4):
        ln3[0] += ln[i][i]
        ln3[1] += ln[i][3-i]
    p = [dumb(ln), dumb(ln2), dumb(ln3)]
    if 'X' in p:
        return 'X won'
    if 'O' in p:
        return 'O won'
    if '.' in p:
        return 'Game has not completed'
    else:
        return 'Draw'
        
inf = open('A-small-attempt0.in', 'r')
outf = open('ans.in', 'w')

no = int(inf.readline())

ln = [1,2,3,4]
for i in range(no):
    for j in range(4):
        ln[j] = inf.readline()
    ans = check(ln)
    outf.write(('Case #{0}: '+ ans + '\n').format(i+1))
    w = inf.readline()

inf.close()
outf.close()
