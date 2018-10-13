def probA():
    f=open('input.txt','r')
    new=open('answer.txt','w')
    for tc in xrange(1, int(f.readline())+1):
        # Get input
        field=""
        for line in xrange(0,3):
            field+=f.readline()[:-1];
        field+=f.readline();
        winner=checkWinner(field)    
        if winner=='X':
            new.write('Case #%d: %s' % (tc,'X won')+"\n")
        elif winner=='O':
            new.write('Case #%d: %s' % (tc,'O won')+"\n")
        elif winner=='Draw':
            new.write('Case #%d: %s' % (tc,'Draw')+"\n")
        else:
            new.write('Case #%d: %s' % (tc,'Game has not completed')+"\n")
        f.readline();
def checkWinner(field):
        # Check rows
        for i in xrange(0,4):
            row=field[i*4:i*4+4]
            if checkO(row):
                return 'O'
            if checkX(row):
                return 'X'
        # Check columns
        for i in xrange(0,4):
            column=field[i]+field[i+4]+field[i+8]+field[i+12]
            if checkO(column):
                return 'O'
            if checkX(column):
                return 'X'
        # Check diagonals

        dia1=field[0]+field[5]+field[10]+field[15]
        dia2=field[3]+field[6]+field[9]+field[12]
        if checkO(dia1) or checkO(dia2):
            return 'O'
        if checkX(dia1) or checkX(dia2):
            return 'X'

        if '.' not in field:
            return 'Draw'

        return 'Not completed'

def checkO(text):
    for char in text:
        if char=='X' or char=='.':
            return False
    return True

def checkX(text):
    for char in text:
        if char=='O' or char=='.':
            return False
    return True

                
