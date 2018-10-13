foo=open("A-large.in","r")
bar=open("tic_op_l.txt","w")
t=int(foo.readline().rstrip())

def row(ch,bingo):
    for x in range(4):
        flag=0
        for y in range(4):
            if bingo[x][y]==ch or bingo[x][y]=='T':
                flag+=1
        if flag==4:
            return True

    return False

def col(ch,bingo):
    for x in range(4):
        flag=0
        for y in range(4):
            if bingo[y][x]==ch or bingo[y][x]=='T':
                flag+=1
        if flag==4:
            return True

    return False
def diag(ch,b) :
    p1 = b[0][0] == ch or b[0][0] == 'T'
    p2 = b[1][1] == ch or b[1][1] == 'T'
    p3 = b[2][2] == ch or b[2][2] == 'T'
    p4 = b[3][3] == ch or b[3][3] == 'T'

    if p1 and p2 and p3 and p4 :
        return True
    
    p1 = b[0][3]== ch or b[0][3] == 'T'
    p2 = b[1][2]== ch or b[1][2] == 'T'
    p3 = b[2][1]== ch or b[2][1] == 'T'
    p4 = b[3][0]== ch or b[3][0] == 'T'

    if p1 and p2 and p3 and p4 :
        return True

    return False
                    
    
    
i=1

while i<=t:
    bingo=[]
    z=0
    ans=''
    dot=False
    while z < 4 :
        line=foo.readline().rstrip()
        if '.' in line :
            dot=True
        bingo.append(line)
        z+=1
    tempLine=foo.readline()

    X = row('X',bingo) or col('X',bingo) or diag('X',bingo)
    O = row('O',bingo) or col('O',bingo) or diag('O',bingo)

    if X :
        ans="Case #"+str(i)+": X won"
    elif O:
        ans="Case #"+str(i)+": O won"
    elif dot:
        ans="Case #"+str(i)+": Game has not completed"
    else:
        ans="Case #"+str(i)+": Draw"
    i+=1

    print ans
    ans=ans+'\n'
    bar.write(ans)
foo.close()
bar.close()
