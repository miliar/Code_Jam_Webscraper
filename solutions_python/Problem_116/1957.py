datain = open('A-large.in', 'r')
dataout = open('dataout.txt', 'w')

# list of possible wins
h_answersX = ['XXXX', 'XXXT', 'XXTX', 'XTXX', 'TXXX']
h_answersO = ['OOOO', 'OOOT', 'OOTO', 'OTOO', 'TOOO']

def check_matrixH(m):    
    # checks matrix horizontally (the transpose of the matrix will handle vertical)
    for i in m:
        if ''.join(i) in h_answersX:
#             print 'hit X on horizontal'
            return 'X'
        elif ''.join(i) in h_answersO:
#             print 'hit O on horizontal'
            return 'O'            
    return ''

def check_matrixV(m):
    m = zip(*m)
    # checks matrix horizontally (the transpose of the matrix makes it check vertical)
    for i in m:
        if ''.join(i) in h_answersX:
#             print 'hit X on vertical'
            return 'X'
        elif ''.join(i) in h_answersO:
#             print 'hit O on vertical'
            return 'O'            
    return ''

def check_matrixD(row1, row2, row3, row4):
    # checking diag
    diagL = row1[0] + row2[1] + row3[2] + row4[3]
    diagR = row4[0] + row3[1] + row2[2] + row1[3]
    diag = [diagL, diagR]
    
    for i in diag:
        if i in h_answersX:
#             print 'hit X on diag'
            return 'X'
        elif i in h_answersO:
#             print 'hit O on diag'
            return 'O'
    return ''

def check_matrixT(row1,row2,row3,row4):
    # checks to see if game is tied or unfinished
    full_row = row1[:4] + row2[:4] + row3[:4] + row4[:4]
#     print 'Full Row: ' + full_row
    
    if '.' in full_row:
        return 'G'
    return 'D'

for length in range(int(datain.readline())):
    row1 = datain.readline()
    row2 = datain.readline()
    row3 = datain.readline()
    row4 = datain.readline()
    blank = datain.readline()
    final = [row1[:4], row2[:4], row3[:4], row4[:4]]

    ''' Section for testing subroutines'''
#     results = check_matrixH(final)                  # confirmed working
#     results = check_matrixV(final)                  # confirmed working
#     results = check_matrixD(row1,row2,row3,row4)    # confirmed working
#     results = check_matrixT(row1,row2,row3,row4)    # confirmed working


    results = check_matrixH(final)
    if len(results) == 0:
        results += check_matrixV(final)
        if len(results) == 0:
            results += check_matrixD(row1,row2,row3,row4)
            if len(results) == 0:
                results += check_matrixT(row1,row2,row3,row4)
    
    print results
    
    if results == 'X':
        dataout.write('Case #' + str(length+1) + ': ' + 'X won' + '\n')
    elif results == 'O':
        dataout.write('Case #' + str(length+1) + ': ' + 'O won' + '\n')
    elif results == 'D':
        dataout.write('Case #' + str(length+1) + ': ' + 'Draw' + '\n')
    elif results == 'G':
        dataout.write('Case #' + str(length+1) + ': ' + 'Game has not completed' + '\n')
    else:
        dataout.write('Case #' + str(length+1) + ': ' + 'ERROR!' + '\n')

datain.close()
dataout.close()