f = open("A-large.in")
answer = open("A-answer-large.txt", 'w')

T = int(f.readline())

for i in xrange(T):
    result = None
    dots = 0
    # read the input    
    case = []
    for j in xrange(5):
        case.append(f.readline().strip())
    
    # determine winner
    
    # rows
    for j in xrange(4):
        r = case[j]
        dots += r.count(".")
        if (r.count("X") == 4) \
            or (r.count("X") == 3 and r.count("T") == 1):
            result = "X won"
            break
        if (r.count("O") == 4) \
            or (r.count("O") == 3 and r.count("T") == 1):
            result = "O won"
            break
        
    # columns
    for j in xrange(4):
        r = case[0][j] + case[1][j] + case[2][j] + case[3][j]
        dots += r.count(".")
        if (r.count("X") == 4) \
            or (r.count("X") == 3 and r.count("T") == 1):
            result = "X won"
            break
        if (r.count("O") == 4) \
            or (r.count("O") == 3 and r.count("T") == 1):
            result = "O won"
            break
    
    # diagonals
    # diagonal 1
    r = case[0][0] + case[1][1] + case[2][2] + case[3][3]
    dots += r.count(".")
    if (r.count("X") == 4) \
        or (r.count("X") == 3 and r.count("T") == 1):
        result = "X won"
    if (r.count("O") == 4) \
        or (r.count("O") == 3 and r.count("T") == 1):
        result = "O won"

    # diagonal 2
    r = case[0][3] + case[1][2] + case[2][1] + case[3][0]
    dots += r.count(".")
    if (r.count("X") == 4) \
        or (r.count("X") == 3 and r.count("T") == 1):
        result = "X won"
    if (r.count("O") == 4) \
        or (r.count("O") == 3 and r.count("T") == 1):
        result = "O won"

    if result == None:
        if dots == 0:
            result = "Draw"
        else:
            result = "Game has not completed"
    answer.write("Case #%d: %s\n" % (i+1, result))

f.close()
answer.close()