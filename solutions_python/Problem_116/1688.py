def check_win(input):
    xwin = False
    owin = False
    dotcount = 0
    inputT = map(list, zip(*input))
    for line in input:
        dotcount = dotcount + line.count('.')
        if line.count('X') == 4 or (line.count('X') == 3 and line.count('T') == 1):
            xwin = True
        if line.count('O') == 4 or (line.count('O') == 3 and line.count('T') == 1):
            owin = True
    for line in inputT:
        dotcount = dotcount + line.count('.')
        if line.count('X') == 4 or (line.count('X') == 3 and line.count('T') == 1):
            xwin = True
        if line.count('O') == 4 or (line.count('O') == 3 and line.count('T') == 1):
            owin = True
    line = [r[i] for i, r in enumerate(input)]
    if line.count('X') == 4 or (line.count('X') == 3 and line.count('T') == 1):
            xwin = True
    if line.count('O') == 4 or (line.count('O') == 3 and line.count('T') == 1):
        owin = True
    
    line = [r[-i-1] for i, r in enumerate(input)]
    if line.count('X') == 4 or (line.count('X') == 3 and line.count('T') == 1):
            xwin = True
    if line.count('O') == 4 or (line.count('O') == 3 and line.count('T') == 1):
        owin = True
    
    if xwin == True:
        return 'X won'
    if owin == True:
        return 'O won'
    if dotcount == 0:
        return 'Draw'
    else:
        return 'Game has not completed'

num = raw_input()
for i in range(0,int(num)):
    input = [[],[],[],[]]
    for line in range(0,4):
        inp = raw_input()
        input[line] = list(inp)
    if i != int(num)-1:
        raw_input()
    print 'Case #'+str(i+1)+': '+check_win(input)
