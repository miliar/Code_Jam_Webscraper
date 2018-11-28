lis = input(': ').replace('O', 'O ').replace('X', 'X ').replace('T', 'T ').replace('.', '. ').split()
if int(lis[0])*16==len(lis)-1:
    lis.remove(lis[0])
    cases = list(zip(*[iter(lis)]*16))
    caseNo = 1
    for case in cases:
        if ((case[0] in ('X', 'T') and case[0] != 'O') and (case[1] in ('X', 'T') and case[1] != 'O') and (case[2] in ('X', 'T') and case[2] != 'O') and (case[3] in ('X', 'T') and case[3] != 'O')) or \
           ((case[4] in ('X', 'T') and case[4] != 'O') and (case[5] in ('X', 'T') and case[5] != 'O') and (case[6] in ('X', 'T') and case[6] != 'O') and (case[7] in ('X', 'T') and case[3] != 'O')) or \
           ((case[8] in ('X', 'T') and case[8] != 'O') and (case[9] in ('X', 'T') and case[9] != 'O') and (case[10] in ('X', 'T') and case[10] != 'O') and (case[11] in ('X', 'T') and case[11] != 'O')) or \
           ((case[12] in ('X', 'T') and case[12] != 'O') and (case[13] in ('X', 'T') and case[13] != 'O') and (case[14] in ('X', 'T') and case[14] != 'O') and (case[15] in ('X', 'T') and case[15] != 'O')) or \
           ((case[0] in ('X', 'T') and case[0] != 'O') and (case[4] in ('X', 'T') and case[4] != 'O') and (case[8] in ('X', 'T') and case[8] != 'O') and (case[12] in ('X', 'T') and case[12] != 'O')) or \
           ((case[1] in ('X', 'T') and case[1] != 'O') and (case[5] in ('X', 'T') and case[5] != 'O') and (case[9] in ('X', 'T') and case[9] != 'O') and (case[13] in ('X', 'T') and case[13] != 'O')) or \
           ((case[2] in ('X', 'T') and case[2] != 'O') and (case[6] in ('X', 'T') and case[6] != 'O') and (case[10] in ('X', 'T') and case[10] != 'O') and (case[14] in ('X', 'T') and case[14] != 'O')) or \
           ((case[3] in ('X', 'T') and case[3] != 'O') and (case[7] in ('X', 'T') and case[7] != 'O') and (case[11] in ('X', 'T') and case[11] != 'O') and (case[15] in ('X', 'T') and case[15] != 'O')) or \
           ((case[0] in ('X', 'T') and case[0] != 'O') and (case[5] in ('X', 'T') and case[5] != 'O') and (case[10] in ('X', 'T') and case[10] != 'O') and (case[15] in ('X', 'T') and case[15] != 'O')) or \
           ((case[3] in ('X', 'T') and case[3] != 'O') and (case[6] in ('X', 'T') and case[6] != 'O') and (case[9] in ('X', 'T') and case[9] != 'O') and (case[12] in ('X', 'T') and case[12] != 'O')):
            print('Case #' + str(caseNo) + ': X won')
        elif ((case[0] in ('O', 'T') and case[0] != 'X') and (case[1] in ('O', 'T') and case[1] != 'X') and (case[2] in ('O', 'T') and case[2] != 'X') and (case[3] in ('O', 'T') and case[3] != 'X')) or \
             ((case[4] in ('O', 'T') and case[4] != 'X') and (case[5] in ('O', 'T') and case[5] != 'X') and (case[6] in ('O', 'T') and case[6] != 'X') and (case[7] in ('O', 'T') and case[3] != 'X')) or \
             ((case[8] in ('O', 'T') and case[8] != 'X') and (case[9] in ('O', 'T') and case[9] != 'X') and (case[10] in ('O', 'T') and case[10] != 'X') and (case[11] in ('O', 'T') and case[11] != 'X')) or \
             ((case[12] in ('O', 'T') and case[12] != 'X') and (case[13] in ('O', 'T') and case[13] != 'X') and (case[14] in ('O', 'T') and case[14] != 'X') and (case[15] in ('O', 'T') and case[15] != 'X')) or \
             ((case[0] in ('O', 'T') and case[0] != 'X') and (case[4] in ('O', 'T') and case[4] != 'X') and (case[8] in ('O', 'T') and case[8] != 'X') and (case[12] in ('O', 'T') and case[12] != 'X')) or \
             ((case[1] in ('O', 'T') and case[1] != 'X') and (case[5] in ('O', 'T') and case[5] != 'X') and (case[9] in ('O', 'T') and case[9] != 'X') and (case[13] in ('O', 'T') and case[13] != 'X')) or \
             ((case[2] in ('O', 'T') and case[2] != 'X') and (case[6] in ('O', 'T') and case[6] != 'X') and (case[10] in ('O', 'T') and case[10] != 'X') and (case[14] in ('O', 'T') and case[14] != 'X')) or \
             ((case[3] in ('O', 'T') and case[3] != 'X') and (case[7] in ('O', 'T') and case[7] != 'X') and (case[11] in ('O', 'T') and case[11] != 'X') and (case[15] in ('O', 'T') and case[15] != 'X')) or \
             ((case[0] in ('O', 'T') and case[0] != 'X') and (case[5] in ('O', 'T') and case[5] != 'X') and (case[10] in ('O', 'T') and case[10] != 'X') and (case[15] in ('O', 'T') and case[15] != 'X')) or \
             ((case[3] in ('O', 'T') and case[3] != 'X') and (case[6] in ('O', 'T') and case[6] != 'X') and (case[9] in ('O', 'T') and case[9] != 'X') and (case[12] in ('O', 'T') and case[12] != 'X')):
            print('Case #' + str(caseNo) + ': O won')
        elif case[0] != '.' and case[1] != '.' and case[2] != '.' and case[3] != '.' and case[4] != '.' and case[5] != '.' and case[6] != '.' and case[7] != '.' and \
             case[8] != '.' and case[9] != '.' and case[10] != '.' and case[11] != '.' and case[12] != '.' and case[13] != '.' and case[14] != '.' and case[15] != '.':
            print('Case #' + str(caseNo) + ': Draw')
        else:
            print('Case #' + str(caseNo) + ': Game has not completed')
        caseNo += 1
else:
    print('Error: Input not of correct size')
