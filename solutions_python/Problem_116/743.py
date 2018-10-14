T = int(raw_input())

def search_horizontal(table, sym):
    cnt = 0
    for i in xrange(0,4):
        for j in xrange(0,4):
            if (table[i][j] == sym or table[i][j] == 'T'): cnt+=1
            else: break
        if (cnt == 4): return True
        else: cnt = 0
    return False

def search_vertical(table, sym):
    cnt = 0
    for i in xrange(0,4):
        for j in xrange(0,4):
            if (table[j][i] == sym or table[j][i] == 'T'): cnt+=1
            else: break
        if (cnt == 4): return True
        else: cnt = 0
    return False

def search_diagonal(table, sym):
    cntl = 0
    cntr = 0
    for i in xrange(0,4):
        if (table[i][i] == sym or table[i][i] == 'T'): cntl+=1

    if (cntl == 4): return True
    j = 0
    for i in xrange(3,-1,-1):
        if (table[j][i] == sym or table[j][i] == 'T'): cntr+=1
        j+=1

    return (cntr == 4)


def still_playing(table):
    for i in xrange(0,4):
        if (table[i].count('.') > 0):
            return True
    return False

if __name__ == "__main__":
    for c in xrange(1,T+1):
        table = []
        for i in xrange(0,4):
            table.append(raw_input())
        if (c < T): raw_input()
        msg = ''
        if (search_horizontal(table, 'O') or \
            search_vertical(table, 'O') or \
            search_diagonal(table, 'O')):
            msg = 'O won'
        elif (search_horizontal(table, 'X') or \
            search_vertical(table, 'X') or \
            search_diagonal(table, 'X')):
            msg = 'X won'
        elif (still_playing(table)):
            msg = 'Game has not completed'
        else:
            msg = 'Draw'

        print 'Case #%d: %s' % (c, msg)

    

