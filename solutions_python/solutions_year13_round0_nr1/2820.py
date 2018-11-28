f = open('input.txt')
games = int(f.readline())
#0 if O wins, 1 if x wins, 2 draw, 3 uncomplete
def checkline(n):
    print n
    t=n[0]
    if t=='T':
        t=n[1]
    for i in n:
        if i =='.':
            return 3
        if i!='T' and i!=t:
            return 2
    if t=='X':
        return 1
    return 0

def checkgame(n):
    checks=[]
    for i in range(4):
        checks.append(checkline([n[r][i] for r in range(4)])) #rows
        checks.append(checkline([n[i][r] for r in range(4)])) #cols
    checks.append(checkline([n[i][i] for i in range(4)]))
    checks.append(checkline([n[i][3-i] for i in range(4)]))
    if 1 in checks:
        return 1
    if 0 in checks:
        return 0
    if 3 in checks:
        return 3
    return 2

win=[]
for i in range(games):
    temp=[]
    for j in range(4):
        temp.append([z for z in f.readline()])
    f.readline()
    win.append(checkgame(temp))
    print temp,'\n'

o=''
for i in range(len(win)):
    o+= 'Case #'+str(i+1)+': '
    if win[i]==0:
        o+='O won\n'
    if win[i]==1:
        o+='X won\n'
    if win[i]==2:
        o+='Draw\n'
    if win[i]==3:
        o+='Game has not completed\n'


out = open('output.txt','w')
out.write(o)
out.close()
