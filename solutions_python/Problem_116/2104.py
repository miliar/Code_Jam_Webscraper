t = int(raw_input())
for x in range(t):
    complete = True
    result_found = False
    count_x = count_o = count_t = 0
    rows = []
    if not x == 0:
        raw_input()
    for i in range(4):
        rows.append(raw_input())
        count_x = count_o = count_t = 0
        for j in range(4):
            if rows[i][j] == 'X':
                count_x += 1
            elif rows[i][j] == 'O':
                count_o += 1
            elif rows[i][j] == 'T':
                count_t += 1
            elif rows[i][j] == '.':
                complete = False
        if (count_x == 4) or (count_x == 3 and count_t == 1):
           print 'Case #%s: %s' %(str(x+1),'X won')
           result_found = True
        if ((count_o == 4) or (count_o == 3 and count_t == 1)) and (not result_found):
           print 'Case #%s: %s' %(str(x+1),'O won')
           result_found = True
    if result_found:
        continue
    for j in range(4):
        count_x = count_o = count_t = 0
        for i in range(4):
            if rows[i][j] == 'X':
                count_x += 1
            elif rows[i][j] == 'O':
                count_o += 1
            elif rows[i][j] == 'T':
                count_t += 1
            elif rows[i][j] == '.':
                complete = False
        if ((count_x == 4) or (count_x == 3 and count_t == 1)) and (not result_found):
           print 'Case #%s: %s' %(str(x+1),'X won')
           result_found = True
        if ((count_o == 4) or (count_o == 3 and count_t == 1)) and (not result_found):
           print 'Case #%s: %s' %(str(x+1),'O won')
           result_found = True
    if result_found:
        continue
    count_x_1 = count_o_1 = count_t_1 = 0
    count_x_2 = count_o_2 = count_t_2 = 0
    for i in range(4):
        if rows[i][i] == 'X':
            count_x_1 += 1
        elif rows[i][i] == 'O':
            count_o_1 += 1
        elif rows[i][i] == 'T':
            count_t_1 += 1
        elif rows[i][i] == '.':
            complete = False

        if rows[i][3-i] == 'X':
            count_x_2 += 1
        elif rows[i][3-i] == 'O':
            count_o_2 += 1
        elif rows[i][3-i] == 'T':
            count_t_2 += 1
        elif rows[i][3-i] == '.':
            complete = False
    if ((count_x_1 == 4) or (count_x_1 == 3 and count_t_1 == 1)) and (not result_found):
        print 'Case #%s: %s' %(str(x+1),'X won')
        result_found = True
    if ((count_o_1 == 4) or (count_o_1 == 3 and count_t_1 == 1)) and (not result_found):
        print 'Case #%s: %s' %(str(x+1),'O won')
        result_found = True
    if ((count_x_2 == 4) or (count_x_2 == 3 and count_t_2 == 1)) and (not result_found):
        print 'Case #%s: %s' %(str(x+1),'X won')
        result_found = True
    if ((count_o_2 == 4) or (count_o_2 == 3 and count_t_2 == 1)) and (not result_found):
        print 'Case #%s: %s' %(str(x+1),'O won')
        result_found = True
    if result_found:
        continue
    if complete == False:
        print 'Case #%s: %s' %(str(x+1),'Game has not completed')
    else:
        print 'Case #%s: %s' %(str(x+1),'Draw')
