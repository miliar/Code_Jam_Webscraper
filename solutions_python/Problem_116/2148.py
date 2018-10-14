
f = open("A-large.in")
num = int(f.readline())
for asdf in range(num):
    board = []
    for n in range(4):
        i = f.readline()
        tmp = []
        for c in i:
            tmp.append(c)
        board.append(tmp)
    
    complete = True
    for y in board:
        if ('.' in y):
            complete = False
            break
            
    skip = False
    #horizontal
    for y in board:
        if ('.' not in y):
            skip = True
            if ('O' in y and not 'X' in y):
                print("Case #"+str(asdf+1)+": O won")
                break
            elif('X' in y and not 'O' in y):
                print("Case #"+str(asdf+1)+": X won")
                break
            elif('O' not in y and 'X' not in y):
                print("Case #"+str(asdf+1)+": Draw")
                break
            else:
                skip = False
    
    #vertical
    if (not skip):
        for x in range(4):
            v = []
            for y in range(4):
                v.append(board[y][x])
            
            if ('.' not in v):
                skip = True
                if ('O' in v and not 'X' in v):
                    print("Case #"+str(asdf+1)+": O won")
                    break
                elif('X' in v and not 'O' in v):
                    print("Case #"+str(asdf+1)+": X won")
                    break
                elif('O' not in v and 'X' not in v):
                    print("Case #"+str(asdf+1)+": Draw")
                    break
                else:
                    skip = False                

    #diag1
    if not skip:
        v = []
        for y in range(4):
            v.append(board[y][y])
            
        if ('.' not in v):
            skip = True
            if ('O' in v and not 'X' in v):
                print("Case #"+str(asdf+1)+": O won")
            elif('X' in v and not 'O' in v):
                print("Case #"+str(asdf+1)+": X won")
            elif('O' not in v and 'X' not in v):
                print("Case #"+str(asdf+1)+": Draw")
            else:
                skip = False        
          
    #diag2  
    if not skip:
        v = []
        for y in range(4):
            v.append(board[3-y][y])
            
        if ('.' not in v):
            skip = True
            if ('O' in v and not 'X' in v):
                print("Case #"+str(asdf+1)+": O won")
            elif('X' in v and not 'O' in v):
                print("Case #"+str(asdf+1)+": X won")
            elif('O' not in v and 'X' not in v):
                print("Case #"+str(asdf+1)+": Draw")
            else:
                skip = False        
            
    if (not skip):
        if complete:
            print("Case #"+str(asdf+1)+": Draw")
        else:
            print("Case #"+str(asdf+1)+": Game has not completed")
    
    i = f.readline()