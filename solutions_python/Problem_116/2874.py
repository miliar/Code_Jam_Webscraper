infile = open('A-small-attempt0.in', 'rU')

casenum = int(infile.readline())

cases = infile.read().strip().split('\n\n')

for i, case in zip(range(1,casenum+1), cases):

    print "Case #" + str(i) + ": ",
    
    case_h = case.split('\n')
    case_v = map(lambda x: reduce(str.__add__, x), zip(*case_h))
    case_d = map(lambda x: ''.join(x), [[c[i][i] for i in range(0,4)] for c in (case_h, map(lambda x: x[::-1], case_h))])
    case_a = reduce(lambda x, y: x.__add__(y), map(lambda x: x, (case_h, case_v, case_d)))

    for player in ('X', 'O'):
        win = False
        for line in case_a:
            if line[:3] == player*3 and line[3] in (player, 'T'):
                win = True
                break
            elif line[1:] == player*3 and line[0] in (player, 'T'):
                win = True
                break
        if win:
            break

    if win:
        print player, 'won'
        continue
    elif '.' in case:
        print 'Game has not completed'
    else:
        print 'Draw'
