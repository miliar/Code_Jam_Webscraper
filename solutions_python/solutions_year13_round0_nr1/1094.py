T = input()
for i in range(T):
    nocomplete = False
    status = [raw_input() for j in range(4)]
    for j in range(4):
        xwon = True
        owon = True
        for k in range(4):
            if status[j][k] == 'O':
                xwon = False
            elif status[j][k] == 'X':
                owon = False
            elif status[j][k] == '.':
                nocomplete = True
                xwon = owon = False
        if xwon or owon:
            break
        xwon = True
        owon = True
        for k in range(4):
            if status[k][j] == 'O':
                xwon = False
            elif status[k][j] == 'X':
                owon = False
            elif status[k][j] == '.':
                nocomplete = True
                xwon = owon = False
        if xwon or owon:
            break
    if not xwon and not owon:
        xwon = True
        owon = True
        for k in range(4):
            if status[k][k] == 'O':
                xwon = False
            elif status[k][k] == 'X':
                owon = False
            elif status[k][k] == '.':
                nocomplete = True
                xwon = owon = False
        if not xwon and not owon:
            xwon = True
            owon = True
            for k in range(4):
                if status[3-k][k] == 'O':
                    xwon = False
                elif status[3-k][k] == 'X':
                    owon = False
                elif status[3-k][k] == '.':
                    nocomplete = True
                    xwon = owon = False
    if xwon:
        print 'Case #'+str(i+1)+': X won'
    elif owon:
        print 'Case #'+str(i+1)+': O won'
    elif nocomplete:
        print 'Case #'+str(i+1)+': Game has not completed'
    else:
        print 'Case #'+str(i+1)+': Draw'
    raw_input()
