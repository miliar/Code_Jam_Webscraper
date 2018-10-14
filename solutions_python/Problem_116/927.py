
def process_input(infile,T):
    for t in range(T):
        vs = []
        for i in range(4):
            vs.append([(0 if v == 'O' else (1 if v == 'X' else (10 if v == 'T' else 100))) for v in infile.readline()[0:-1]])
        try:
            infile.readline()
        except:
            pass
        yield vs


infile = open('A-large.in','r')
T = int(infile.readline())
vs = process_input(infile,T)
for t in range(T):
    v = vs.next()
    winner = ''
    for r in v:
        s = sum(r)
        if s == 0 or s == 10:
            winner = 'O'
            break
        elif s == 4 or s == 13:
            winner = 'X'
            break
    if winner == '':
        for r in zip(*v):
            s = sum(r)
            if s == 0 or s == 10:
                winner = 'O'
                break
            elif s == 4 or s == 13:
                winner = 'X'
                break
        if winner == '':
            s = v[0][0]+v[1][1]+v[2][2]+v[3][3]
            if s == 0 or s == 10:
                winner = 'O'
            elif s == 4 or s == 13:
                winner = 'X'
            if winner == '':
                s = v[0][3]+v[1][2]+v[2][1]+v[3][0]
                if s == 0 or s == 10:
                    winner = 'O'
                elif s == 4 or s == 13:
                    winner = 'X'
    if winner == '':
        for r in v:
            s = sum(r)
            if s > 100:
                winner = 'G'
                break
        if winner == 'G':
            print 'Case #'+str(t+1)+': Game has not completed'
        else:
            print 'Case #'+str(t+1)+': Draw'
    elif winner == 'X':
        print 'Case #'+str(t+1)+': X won'
    else:
        print 'Case #'+str(t+1)+': O won'
        
                
            
