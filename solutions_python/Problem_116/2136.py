inputs = filter(lambda x: x!='', map(lambda x: x.strip(), open('A-large.in', 'r').readlines()))[1:]
output = open('output.txt', 'w')
line_cnt = 0
case_cnt = 1
while line_cnt < len(inputs): 
    input = inputs[line_cnt:line_cnt+4]
    winner = "Game has not completed"
    flatten = reduce(lambda sublist1, sublist2: sublist1 + sublist2, input)
    if not '.' in flatten:
        winner = "Draw"
    
    matrix = []
    for line in input:
        row = []
        for c in line:
            row.append(c)
        matrix.append(row)
    
    def has_won(elements):
        '''
        takes 4 elements and determines if there someone won
        '''
        cnt_t, cnt_x, cnt_o = 0,0,0
        for ele in elements:
            if ele == 'X':
                cnt_x += 1
            elif ele == 'O':
                cnt_o += 1
            elif ele == 'T':
                cnt_t += 1
        if cnt_x == 4 or cnt_x + cnt_t == 4:
            return 'X won'
        elif cnt_o == 4 or cnt_o + cnt_t == 4:
            return 'O won'
        else:
            return False
        
    
            
    for row in matrix:
        won = has_won(row)
        if won:
            winner = won
    
    cols = []
    for i in range(4):
        tmp = []
        for j in range(4):
            tmp.append(matrix[j][i])
        cols.append(tmp)
    
    for col in cols:
        won = has_won(col)
        if won:
            winner = won
    
    diags = [
             [matrix[0][0], matrix[1][1], matrix[2][2], matrix[3][3]],
             [matrix[0][3], matrix[1][2], matrix[2][1], matrix[3][0]],
             [matrix[0][1], matrix[1][2], matrix[2][3]],
             [matrix[1][0], matrix[2][1], matrix[3][2]],
             [matrix[0][2], matrix[1][1], matrix[2][0]],
             [matrix[1][3], matrix[2][2], matrix[3][1]],
             ]
    for diag in diags:
        won = has_won(diag)
        if won:
            winner = won
    output.write("Case #%i: %s\n" % (case_cnt, winner))
    case_cnt += 1
    line_cnt += 4


