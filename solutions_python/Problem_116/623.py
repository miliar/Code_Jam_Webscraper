fd = file('A-small-attempt0.in')
totalTestCase = int(fd.readline())
def replace_symbol(s):
    return s.replace('.', '1').replace('X', '2') \
            .replace('O', '3').replace('T', '4')
def genTestCase(fd):
    global totalTestCase
    while totalTestCase > 0:
        tbl = []
        #row
        r1 = fd.readline().strip()
        r2 = fd.readline().strip()
        r3 = fd.readline().strip()
        r4 = fd.readline().strip()
        #column
        c1 = r1[0]+r2[0]+r3[0]+r4[0]
        c2 = r1[1]+r2[1]+r3[1]+r4[1]
        c3 = r1[2]+r2[2]+r3[2]+r4[2]
        c4 = r1[3]+r2[3]+r3[3]+r4[3]
        #diagnol
        d1 = r1[0]+r2[1]+r3[2]+r4[3]
        d2 = r1[3]+r2[2]+r3[1]+r4[0]
        #append all situation
        tbl_row = [replace_symbol(r1),
                   replace_symbol(r2),
                   replace_symbol(r3),
                   replace_symbol(r4)]
        tbl_col = [replace_symbol(c1),
                   replace_symbol(c2),
                   replace_symbol(c3),
                   replace_symbol(c4)]
        tbl_diag =[replace_symbol(d1),
                   replace_symbol(d2)]
        fd.readline()
        totalTestCase -= 1
        yield (tbl_row, tbl_col, tbl_diag)
    fd.close()
tc_seq = 1
for (tbl_row, tbl_col, tbl_diag) in genTestCase(fd):
    #process 4 row
    playerx_win = set([2222, 2224, 2242, 2422, 4222]) 
    playero_win = set([3333, 3334, 3343, 2422, 4333])
    not_complete = False
    playerx_win1 = False
    playero_win1 = False
    all_situation = set(tbl_row+tbl_col+tbl_diag)
    for s in all_situation:
        s = int(s)
        if s in playerx_win:
            #print 'Case #%d: X won'%tc_seq
            playerx_win1 =True
        elif s in playero_win:
            #print 'Case #%d: O won'%tc_seq
            playero_win1 =True
        else:
            if s%10 == 1:
                not_complete = True
                continue
            else:
                s = s/10
            if s%10 == 1:
                not_complete = True
                continue
            else:
                s = s/10
            if s%10 == 1:
                not_complete = True
                continue
            else:
                s = s/10
            if s%10 == 1:
                not_complete = True
                continue
            else:
                pass
    if playerx_win1:
        print 'Case #%d: X won'%tc_seq
        pass
    elif playero_win1:
        print 'Case #%d: O won'%tc_seq
    elif not_complete:
        print 'Case #%d: Game has not completed'%tc_seq
    else:
        print 'Case #%d: Draw'%tc_seq 
    tc_seq += 1