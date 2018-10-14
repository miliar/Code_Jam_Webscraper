f=open(r'A-large.in','r')
test_cases=int(f.readline().strip())
#test_cases=input()
#print test_cases
def game_state():
    x_win=0
    o_win=0
    draw=0
    completed=0
    for x in range(0,4):
        row=[s for s in grid[x]]
        if 'T' in row:
            row.remove('T')
        symbol=row[0]
        win=1
        #print row
        for y in row:
            if y==symbol and win:
                win=1
            else:
                win=0
        if win:
            if symbol=='X':
                x_win=1
                #print row,'row'
                return "X"
            elif symbol=='O':
                o_win=1
                #print row,'row'
                return "O"
    if x_win!=1 and o_win!=1:
        for x in range(0,4):
            column=[r[x] for r in grid]
            if 'T' in column:
                column.remove('T')
            symbol=column[0]
            win=1
            for y in column:
                if y==symbol and win:
                    win=1
                else:
                    win=0
            if win:
                if symbol=='X':
                    x_win=1
                    #print 'col'
                    return "X"
                elif symbol=='O':
                    o_win=1
                    #print column,'col'
                    return "O"
    if x_win!=1 and o_win!=1:
        diagonal1=[]
        diagonal2=[]
        diagonals=[]
        for x in range(0,4):
            diagonal1.append(grid[x][x])
            diagonal2.append(grid[x][3-x])
        diagonals.append(diagonal1)
        diagonals.append(diagonal2)
        for diagonal in diagonals:
            if 'T' in diagonal:
                diagonal.remove('T')
            symbol=diagonal[0]
            win=1
            for y in diagonal:
                if y==symbol and win:
                    win=1
                else:
                    win=0
            if win:
                if symbol=='X':
                    x_win=1
                    #print 'col'
                    return "X"
                elif symbol=='O':
                    o_win=1
                    #print column,'col'
                    return "O"
        
    for x in grid:
        for y in x:
            if y=='.':
                return 'C'
    return 'D'
            
            
        


for x in range(1,test_cases+1):
    grid=[]
    for y in range(0,4):
        #line=raw_input()
        line=f.readline().strip()
        line=list(line)
        grid.append(line)
    result=game_state()
    if result=='X':
        print 'Case #%d: X won'%x
    if result=='O':
        print 'Case #%d: O won'%x
    if result=='D':
        print 'Case #%d: Draw'%x
    if result=='C':
        print 'Case #%d: Game has not completed'%x
    blank=f.readline()
    #blank=raw_input()
    
