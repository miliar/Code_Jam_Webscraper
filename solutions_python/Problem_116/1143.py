f = open('A-large.in', 'r')
g = open('output.txt', 'w')
n = int(f.readline())
for i in range (1, n+1):
    found = False
    board = []
    for x in range (0, 4):
        string = f.readline()
        for y in range (0, 4):
            board.append(string[y])
    f.readline()
    for x in range (0, 4):
        c1 = board[x]
        c2 = board[x+4]
        c3 = board[x+8]
        c4 = board[x+12]
        if c1 == '.' or c2 == '.' or c3 == '.' or c4 == '.':
            continue
        if c1 == 'T':
            c1 = c2
        else:
            if c2 == 'T':
                c2 = c1
            elif c3 == 'T': 
                c3 = c1
            elif c4 == 'T':
                c4 = c1                
        if c1 == c2 and c2 == c3 and c4 == c3: 
            line = 'Case #' + str(i) + ': ' + c1 + ' won\n'
            g.write(line)  
            found = True 
            break
    if found:
        continue
    for x in range (0, 4):
        k = 4*x
        c1 = board[k]
        c2 = board[k+1]
        c3 = board[k+2]
        c4 = board[k+3]
        if c1 == '.' or c2 == '.' or c3 == '.' or c4 == '.':
            continue
        if c1 == 'T':
            c1 = c2
        else:
            if c2 == 'T':
                c2 = c1
            elif c3 == 'T': 
                c3 = c1
            elif c4 == 'T':
                c4 = c1                
        if c1 == c2 and c2 == c3 and c4 == c3: 
            line = 'Case #' + str(i) + ': ' + c1 + ' won\n'
            g.write(line)
            found = True
            break
    if not found: 
        period = True
        c1 = board[0]
        c2 = board[5]
        c3 = board[10]
        c4 = board[15]
        if c1 == '.' or c2 == '.' or c3 == '.' or c4 == '.':
            period = False
        elif c1 == 'T':
            c1 = c2
        else:
            if c2 == 'T':
                c2 = c1
            elif c3 == 'T': 
                c3 = c1
            elif c4 == 'T':
                c4 = c1                
        if c1 == c2 and c2 == c3 and c4 == c3 and period: 
            line = 'Case #' + str(i) + ': ' + c1 + ' won\n'
            g.write(line)
            found = True
    if not found:
        period = True
        c1 = board[3]
        c2 = board[6]
        c3 = board[9]
        c4 = board[12]
        if c1 == '.' or c2 == '.' or c3 == '.' or c4 == '.':
            period = False
        elif c1 == 'T':
            c1 = c2
        else:
            if c2 == 'T':
                c2 = c1
            elif c3 == 'T': 
                c3 = c1
            elif c4 == 'T':
                c4 = c1                
        if c1 == c2 and c2 == c3 and c4 == c3 and period: 
            line = 'Case #' + str(i) + ': ' + c1 + ' won\n'
            g.write(line) 
            found = True
    if not found:
        if '.' in board:
            line = 'Case #' + str(i) + ': Game has not completed\n'
            g.write(line) 
        else: 
            line = 'Case #' + str(i) + ': Draw\n'
            g.write(line) 
f.close()
g.close()