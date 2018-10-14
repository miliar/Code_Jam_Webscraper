def A():
    f = open('A-small-attempt1.in')
    T = int(f.readline())
    
    for t in range(T):
        #===Reading File=============================================================
        tmp = []
        tmp.append(f.readline())
        tmp.append(f.readline())
        tmp.append(f.readline())
        tmp.append(f.readline())
        emptyLine = f.readline()
        anyBodyWon = False
        isDone = True
        #============================================================================

        #===Test Cases for not 'T' in the board======================================
        for i in range(4):
            testCase = tmp[i]
            #---Checking Line
            if tmp[i][0] == tmp[i][1] == tmp[i][2] == tmp[i][3] and tmp[i][0]!='.':
                print 'Case #' + str(t+1) + ': ' + tmp[i][0] + ' won'
                anyBodyWon = True
            #---Checking Col
            elif tmp[0][i] == tmp[1][i] == tmp[2][i] == tmp[3][i] and tmp[0][i]!='.':
                print 'Case #' + str(t+1) + ': ' + tmp[0][i] + ' won'
                anyBodyWon = True
            #---Checking to see if the square boared is completed
            if '.' in testCase:
                isDone = False
        #---Checking diagonal
        if tmp[0][0] == tmp[1][1] == tmp[2][2] == tmp[3][3] and tmp[0][0]!='.':
            print 'Case #' + str(t+1) + ': ' + tmp[0][0] + ' won'
            anyBodyWon = True
        elif tmp[0][3] == tmp[1][2] == tmp[2][1] == tmp[3][0] and tmp[0][3]!='.':
            print 'Case #' + str(t+1) + ': ' + tmp[0][3] + ' won'
            anyBodyWon = True
        #============================================================================
        
        #===Test Cases for existance of 'T'==========================================
        for i in range(4):
            TLoc = tmp[i].find('T')
            if TLoc != -1:
                #---Checking Line
                test = tmp[i]
                test.replace('T', '')
                if test[0] == test[1] == test[2] and test[0]!='.':
                    print 'Case #' + str(t+1) + ': ' + test[0] + ' won'
                    anyBodyWon = True
                #---Checking Col
                x = [0, 1, 2, 3]
                x.remove(i)
                if tmp[x[0]][TLoc] == tmp[x[1]][TLoc] == tmp[x[2]][TLoc] and tmp[x[0]][TLoc]!='.':
                    print 'Case #' + str(t+1) + ': ' + tmp[x[0]][TLoc] + ' won'
                    anyBodyWon = True
        #---Checking diagonal
        diagonal = [[tmp[0][0],tmp[1][1],tmp[2][2],tmp[3][3]],[tmp[0][3],tmp[1][2],tmp[2][1],tmp[3][0]]]
        if 'T'in diagonal[0]:
            diagonal[0].remove('T')
            if diagonal[0][0] == diagonal[0][1] == diagonal[0][2] and diagonal[0][0]!='.':
                print 'Case #' + str(t+1) + ': ' + diagonal[0][0] + ' won'
                anyBodyWon = True
        elif 'T'in diagonal[1]:
            diagonal[1].remove('T')
            if diagonal[1][0] == diagonal[1][1] == diagonal[1][2] and diagonal[1][0]!='.':
                print 'Case #' + str(t+1) + ': ' + diagonal[1][0] + ' won'
                anyBodyWon = True
        #============================================================================

        if anyBodyWon == False and isDone == False:
            print 'Case #' + str(t+1) + ': Game has not completed'
        elif anyBodyWon == False and isDone == True:
            print 'Case #' + str(t+1) + ': Draw'
        
