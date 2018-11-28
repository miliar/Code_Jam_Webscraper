#run with "python2 problemA.py <inputfile >outputfile" on arch linux

cases = input("")

for case in range(cases):
    matrix = []
    #get input
    for i in range(4):
        matrix.append(raw_input())
    if case != cases-1:
        raw_input()
        
    #check X win
    #diagonal
    won = True
    for i in range(4):
        if matrix[i][i] in "XT":
            pass
        else:
            won = False
    if won:
        print "Case #%s: X won" %(case+1)
        continue
    
    #other diagonal
    won = True
    for i in range(4):
        if matrix[i][3-i] in "XT":
            pass
        else:
            won = False    
    if won:
        print "Case #%s: X won" %(case+1)
        continue
        
    #rows & columns
    for i in range(4):
        won = True
        for j in range(4):
            if matrix[i][j] in "XT":
                pass
            else:
                won = False
        if won:
            print "Case #%s: X won" %(case+1)
            break
    if won:
        continue
        
    for i in range(4):
        won = True
        for j in range(4):
            if matrix[j][i] in "XT":
                pass
            else:
                won = False
        if won:
            print "Case #%s: X won" %(case+1)
            break        
    if won:
        continue    

    #O wins                    
    won = True
    for i in range(4):
       if matrix[i][i] in "OT":
            pass
       else:
            won = False
    if won:
        print "Case #%s: O won" %(case+1)
        continue
    
    #other diagonal
    won = True
    for i in range(4):
        if matrix[i][3-i] in "OT":
            pass
        else:
            won = False    
    if won:
        print "Case #%s: O won" %(case+1)
        continue
        
    #rows & columns
    for i in range(4):
        won = True
        for j in range(4):
            if matrix[i][j] in "OT":
                pass
            else:
                won = False
        if won:
            print "Case #%s: O won" %(case+1)
            break
    if won:
        continue
        
    for i in range(4):
        won = True
        for j in range(4):
            if matrix[j][i] in "OT":
                pass
            else:
                won = False
        if won:
            print "Case #%s: O won" %(case+1)
            break        
    if won:
        continue    
                    
    #draw or uncomplete
    uncomplete = False
    for i in range(4):
        for j in range(4):
            if matrix[i][j]==".":
                uncomplete = True
    if uncomplete:
        print "Case #%s: Game has not completed" %(case+1)
    else:
        print "Case #%s: Draw" %(case+1)
