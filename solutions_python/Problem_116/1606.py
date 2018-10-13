def who_won(win):
    if win == 'X':
        print 'X won' 
    else:
        print 'O won' 


with open('A-small-attempt3.in') as f:
    cases = int(f.readline())

    for i in xrange(cases):
        a = []
        print 'Case #%s:' % (i+1),
        for j in xrange(4):
            a.append(f.readline().strip())
        waste = f.readline()

        not_finished = False
        has_result = False

        for j in xrange(4):
            win = a[j][0]
            if win == '.':
                not_finished=True
                continue
            if win == 'T':
                win = a[j][1]
            for k in xrange(4):
                if a[j][k] != win and a[j][k]!='T':
                    win = ''
                if a[j][k] == '.':
                    not_finished = True

            if win != '':
                who_won(win)
                has_result = True
                continue

        if has_result:
            continue

        for j in xrange(4):
            win = a[0][j]
            if win == '.':
                continue
            if win == 'T':
                win = a[1][j]
            for k in xrange(4):
                if a[k][j] != win and a[k][j]!='T':
                    win = ''
            if win != '':
                who_won(win)
                has_result = True
                continue
        
        if has_result:
            continue

        win = a[0][0]
        if win == 'T':
            win = a[1][1]
        for j in xrange(4):
            if a[j][j] != win and a[j][j]!='T':
                win = ''
        if win != '' and win != '.':
            who_won(win)
            continue

        win = a[0][3]
        if win == 'T':
            win = a[1][2]
        for j in xrange(4):
            if a[j][3-j] != win and a[j][3-j]!='T':
                win = ''
        if win != '' and win != '.':
            who_won(win)
            continue

        if not_finished:
            print 'Game has not completed'
        else:
            print 'Draw'


    


