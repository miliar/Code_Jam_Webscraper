input_file = open("A-large.in", "r")
cases = int(input_file.readline())
for case in range(0, cases):
    
    num = 1
    
    xwin = [[0,[1,2,3,4]],[0,[1,6,11,16]],[0,[1,5,9,13]],[0,[2,6,10,14]],[0,[3,7,11,15]],[0,[4,8,12,16]],[0,[4,7,10,13]],[0,[5,6,7,8]],[0,[9,10,11,12]],[0,[13,14,15,16]]]
    
    owin = [[0,[1,2,3,4]],[0,[1,6,11,16]],[0,[1,5,9,13]],[0,[2,6,10,14]],[0,[3,7,11,15]],[0,[4,8,12,16]],[0,[4,7,10,13]],[0,[5,6,7,8]],[0,[9,10,11,12]],[0,[13,14,15,16]]]    
    
    owins = False
    xwins = False
    draw = True
        
    board = [input_file.readline(), input_file.readline(), input_file.readline(), input_file.readline()]
    for row in board:
        for move in row:
            move = move.lower()
            if not (owins or xwins):
                if move == '.':
                    draw = False
                    num += 1
                elif move == 't':
                    for win in xwin:
                        if win[1][win[0]] == num:
                            win[0] += 1
                            if win[0] >= 4:
                                xwins = True
                    for win in owin:
                        if win[1][win[0]] == num:
                            win[0] += 1
                            if win[0] >= 4:
                                owins = True
                    num += 1
                elif move == 'x':
                    for win in xwin:
                        if win[1][win[0]] == num:
                            win[0] += 1
                            if win[0] >= 4:
                                xwins = True
                    num += 1
                elif move == 'o':
                    for win in owin:
                        if win[1][win[0]] == num:
                            win[0] += 1
                            if win[0] >= 4:
                                owins = True
                    num += 1
    if xwins:
        print ("Case #%d: X won" %(case + 1))
    elif owins:
        print ("Case #%d: O won" %(case + 1))
    elif draw:
        print ("Case #%d: Draw" %(case + 1))
    else:
        print ("Case #%d: Game has not completed" %(case + 1))
        
    input_file.readline()

input_file.close()
    