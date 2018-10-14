import string

def solve(field):
    #check lines
    x = 0
    o = 0
    t = 0
    dot = 0
    unfinished = False
    for line in field:
        x = string.count(line[0], "X") 
        o = string.count(line[0], "O") 
        t = string.count(line[0], "T") 
        dot = string.count(line[0], ".") 
        if dot > 0:
            unfinished = True
        if x + t == 4:
            return "X won"
        if o + t == 4:
            return "O won"

    x = 0
    o = 0
    t = 0
    for row in range(4):
        r = ""
        for c in range(4):
            r += field[c][0][row]
        x = string.count(r, "X") 
        o = string.count(r, "O") 
        t = string.count(r, "T") 
        dot = string.count(r, ".") 
        if dot > 0:
            unfinished = True
        if x + t == 4:
            return "X won"
        if o + t == 4:
            return "O won"

    x = 0
    o = 0
    t = 0
    r = ""
    for c in range(4):
        r += field[c][0][c]
    x = string.count(r, "X") 
    o = string.count(r, "O") 
    t = string.count(r, "T") 
    dot = string.count(r, ".") 
    if dot > 0:
        unfinished = True
    if x + t == 4:
        return "X won"
    if o + t == 4:
        return "O won"

    x = 0
    o = 0
    t = 0
    r = ""
    for c in range(4):
        r += field[3-c][0][c]
    x = string.count(r, "X") 
    o = string.count(r, "O") 
    t = string.count(r, "T") 
    dot = string.count(r, ".") 
    if dot > 0:
        unfinished = True
    if x + t == 4:
        return "X won"
    if o + t == 4:
        return "O won"

    if unfinished:
        return "Game has not completed"
    return "Draw"
        
        



f = open('a.in')
T = int(f.readline())
for t in range(T):

    field = []
    field.append(f.readline().split())
    field.append(f.readline().split())
    field.append(f.readline().split())
    field.append(f.readline().split())
    f.readline()
    result = solve(field)


            
    print "Case #%d: %s" % (t+1, result)
