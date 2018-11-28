f = open('A-large.in', 'r')

case = int(f.readline())
board = ''
x=['X', 'T']
o=['O', 'T']
def gres(b):
    if (b[0] in x) and (b[5] in x) and (b[10] in x) and (b[15] in x):
        return 'x'

    if (b[3] in x) and (b[6] in x) and (b[9] in x) and (b[12] in x):
        return 'x'

    if (b[0] in o) and (b[5] in o) and (b[10] in o) and (b[15] in o):
        return 'o'

    if (b[3] in o) and (b[6] in o) and (b[9] in o) and (b[12] in o):
        return 'o'

    for i in range(4):
        if (b[i] in x) and (b[i+4] in x) and (b[i+8] in x) and (b[i+12] in x):
            return 'x'

        if (b[i] in o) and (b[i+4] in o) and (b[i+8] in o) and (b[i+12] in o):
            return 'o'

        j = i*4
        bs = b[j:j+4]
        if (bs.find('O') == -1 and bs.find('.') == -1):
            return 'x'

        if (bs.find('X') == -1 and bs.find('.') == -1):
            return 'o'

    if b.find('.') == -1:
        return 'd'
    else:
        return 'n'

    
fw = open('A-large.out', 'w')


for i in range(case):
    for j in range(4):
        
        if j==0:
            board = f.readline()[0:4]
        else:
            board = board + f.readline()[0:4]
        
    result = gres(board)
    cn = i+1
    if result == 'x':
        fw.write('Case #%d: X won\n' % cn)
    elif result == 'o':
        fw.write('Case #%d: O won\n' % cn)
    elif result == 'd':
        fw.write('Case #%d: Draw\n' % cn)
    else:
        fw.write('Case #%d: Game has not completed\n' % cn)
    f.readline()

f.close()
fw.close()    
