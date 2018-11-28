f = open(r"/home/cr0byt3ch/Downloads/A-large.in")
g = open("/home/cr0byt3ch/Desktop/output3.out", 'w')

case_no = int(f.readline().rstrip('\n'))
def tic_toe(i):
    state = ""
    for j in range(4):
        state += f.readline().rstrip('\n')
     #taking care of the first diagonal
    temp = state[0] + state[5] + state[10] +state[15]
    if  sorted(temp) == sorted('TXXX') or sorted(temp) == sorted('XXXX'):
        g.writelines('Case #' +str(i) +': X won' + '\n')
        return 0;
    if  sorted(temp) == sorted('OOOT') or sorted(temp) == sorted('OOOO'):
        g.writelines('Case #' +str(i) +': O won'+ '\n')
        return 0;
    #taking care of the second diagonal
    temp = state[3] + state[6] + state[9] +state[12]
    if  sorted(temp) == sorted('TXXX') or sorted(temp) == sorted('XXXX'):
            g.writelines('Case #' +str(i) +': X won'+ '\n')
            return 0;
    if  sorted(temp) == sorted('OOOT') or sorted(temp) == sorted('OOOO'):
            g.writelines('Case #' +str(i) +': O won'+ '\n')
            return 0;
    #for horizontal and vertical checks
    
    temp = state[0] + state[1] + state[2] +state[3]
    if  sorted(temp) == sorted('TXXX') or sorted(temp) == sorted('XXXX'):
        g.writelines('Case #' +str(i) +': X won' + '\n')
        return 0;
    if  sorted(temp) == sorted('OOOT') or sorted(temp) == sorted('OOOO'):
        g.writelines('Case #' +str(i) +': O won'+ '\n')
        return 0;
    temp = state[4] + state[5] + state[6] +state[7]
    if  sorted(temp) == sorted('TXXX') or sorted(temp) == sorted('XXXX'):
        g.writelines('Case #' +str(i) +': X won' + '\n')
        return 0;
    if  sorted(temp) == sorted('OOOT') or sorted(temp) == sorted('OOOO'):
        g.writelines('Case #' +str(i) +': O won'+ '\n')
        return 0;
    temp = state[8] + state[9] + state[10] +state[11]
    if  sorted(temp) == sorted('TXXX') or sorted(temp) == sorted('XXXX'):
        g.writelines('Case #' +str(i) +': X won' + '\n')
        return 0;
    if  sorted(temp) == sorted('OOOT') or sorted(temp) == sorted('OOOO'):
        g.writelines('Case #' +str(i) +': O won'+ '\n')
        return 0;
    temp = state[12] + state[13] + state[14] +state[15]
    if  sorted(temp) == sorted('TXXX') or sorted(temp) == sorted('XXXX'):
        g.writelines('Case #' +str(i) +': X won' + '\n')
        return 0;
    if  sorted(temp) == sorted('OOOT') or sorted(temp) == sorted('OOOO'):
        g.writelines('Case #' +str(i) +': O won'+ '\n')
        return 0;
    #vertical checks:
    temp = state[0] + state[4] + state[8] +state[12]
    if  sorted(temp) == sorted('TXXX') or sorted(temp) == sorted('XXXX'):
            g.writelines('Case #' +str(i) +': X won'+ '\n')
            return 0;
    if  sorted(temp) == sorted('OOOT') or sorted(temp) == sorted('OOOO'):
            g.writelines('Case #' +str(i) +': O won'+ '\n')
            return 0;
    temp = state[1] + state[5] + state[9] +state[13]
    if  sorted(temp) == sorted('TXXX') or sorted(temp) == sorted('XXXX'):
            g.writelines('Case #' +str(i) +': X won'+ '\n')
            return 0;
    if  sorted(temp) == sorted('OOOT') or sorted(temp) == sorted('OOOO'):
            g.writelines('Case #' +str(i) +': O won'+ '\n')
            return 0;
    temp = state[2] + state[6] + state[10] +state[14]
    if  sorted(temp) == sorted('TXXX') or sorted(temp) == sorted('XXXX'):
            g.writelines('Case #' +str(i) +': X won'+ '\n')
            return 0;
    if  sorted(temp) == sorted('OOOT') or sorted(temp) == sorted('OOOO'):
            g.writelines('Case #' +str(i) +': O won'+ '\n')
            return 0;
    temp = state[3] + state[7] + state[11] +state[15]
    if  sorted(temp) == sorted('TXXX') or sorted(temp) == sorted('XXXX'):
            g.writelines('Case #' +str(i) +': X won'+ '\n')
            return 0;
    if  sorted(temp) == sorted('OOOT') or sorted(temp) == sorted('OOOO'):
            g.writelines('Case #' +str(i) +': O won'+ '\n')
            return 0;
    #if after horizontal, vertical and diagonal checks there isn't a winner then the game is either a draw or is incomplete
    #if there is no ., then the game is a draw   
    if state.count('.')== 0:
            g.writelines('Case #' +str(i) +': Draw'+ '\n')
            return 0
    if state.count('.') is not 0:
            g.writelines('Case #' +str(i)+': Game has not completed'+ '\n')
            return 0
        
for i in range(case_no):
    tic_toe(i+1)
    f.readline()
g.writelines('\n')
g.close()
f.close()
    
    
    
    