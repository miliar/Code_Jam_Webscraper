from sys import stdin

cases = int(stdin.readline().strip())

xwin = "X won"
owin = "O won"
draw = "Draw"
not_done = "Game has not completed"

def state(lines):
    for x in xrange(4):
        all_x = True; all_o = True
        for y in xrange(4):
            if lines[x][y] == 'O':
                all_x = False
            elif lines[x][y] == 'X':
                all_o = False
            elif lines[x][y] == '.':
                all_o = False
                all_x = False
        if all_x: return xwin
        if all_o: return owin

    for y in xrange(4):
        all_x = True; all_o = True
        for x in xrange(4):
            if lines[x][y] == 'O':
                all_x = False
            elif lines[x][y] == 'X':
                all_o = False
            elif lines[x][y] == '.':
                all_o = False
                all_x = False
        if all_x: return xwin
        if all_o: return owin

    all_x = True; all_o = True
    for x in xrange(4):
        if lines[x][x] == 'O':
            all_x = False
        elif lines[x][x] == 'X':
            all_o = False
        elif lines[x][x] == '.':
            all_o = False
            all_x = False
    if all_x: return xwin
    if all_o: return owin

    all_x = True; all_o = True
    for x in xrange(4):
        if lines[x][3-x] == 'O':
            all_x = False
        elif lines[x][3-x] == 'X':
            all_o = False
        elif lines[x][3-x] == '.':
            all_o = False
            all_x = False
    if all_x: return xwin
    if all_o: return owin
        
    filled = '.' not in ''.join(lines)
    if filled: return draw
    return not_done

for case in xrange(1, cases+1):
    lines = []
    for row in xrange(4):
        lines.append(stdin.readline().strip())
    # ignore blank
    try: stdin.readline()
    except: pass

    outcome = state(lines)
    print "Case #%d: %s" % (case, outcome)



