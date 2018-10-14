fin = open('in.txt','r')
fout = open('out.txt','w')

n = int(fin.readline())
winX = ['XXXX','TXXX']
winO = ['OOOO','OOOT']

def state(s):    
    for i in range(len(s)):
        tr = ''.join(sorted(s[i]))
        tc = ''.join(sorted(zip(*s)[i]))
        if tr in winX or tc in winX:
            return 'X won'
        elif tr in winO or tc in winO:
            return 'O won'
        
    ldiag = ''.join(sorted([s[0][0],s[1][1],s[2][2],s[3][3]]))
    rdiag = ''.join(sorted([s[0][3],s[1][2],s[2][1],s[3][0]]))
    if ldiag in winX or rdiag in winX:
        return 'X won'
    elif ldiag in winO or rdiag in winO:
        return 'O won'
    
    for i in range(len(s)):
        if '.' in s[i]:
            return 'Game has not completed'
    return 'Draw'

for i in range(n):
    board = []
    for j in range(4):
        board.append(list(fin.readline().strip()))
    fout.write('Case #%d: %s\n'%(i+1,state(board)))
    fin.readline()

fin.close()
fout.close()
    
