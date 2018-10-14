def solve(graph):
    oWin = False
    xWin = False
    # for i in range(4):
        # print graph[i]
    for i in range(4):
        s = sum(graph[i])
        if s == 40 or s == 130:
            oWin = True
        if s == 4 or s == 103:
            xWin = True
        s = sum([graph[j][i] for j in range(4)])  
        if s == 40 or s == 130:
            oWin = True
        if s == 4 or s == 103:
            xWin = True
    s = sum([graph[i][i] for i in range(4)])
    if s == 40 or s == 130:
        oWin = True
    if s == 4 or s == 103:
        xWin = True
    s = sum([graph[3 - i][i] for i in range(4)])
    if s == 40 or s == 130:
        oWin = True
    if s == 4 or s == 103:
        xWin = True
        xWin = True
    if xWin and oWin:
        print "==== both wins!!!!!"
        return "Draw"
    elif xWin:
        return "X won"
    elif oWin:
        return "O won"

    draw = True
    for i in range(4):
        for j in range(4):
            if graph[i][j] == 0:
                draw = False
                break
    if draw:
        return "Draw"
    return "Game has not completed"

f = open('Aoutput.in', 'r')
out = open('Aoutput', 'w')
l = f.readline()
num = int(l)
for i in range(num):
    graph = [[0 for b in range(4)] for a in range(4)]
    for j in range(4):
        l = f.readline()
        for k in range(4):
            if l[k] == 'X':
                graph[j][k] = 1
            elif l[k] == 'T':
                graph[j][k] = 100
            elif l[k] == 'O':
                graph[j][k] = 10
    f.readline()
    # import pdb; pdb.set_trace()
    print "Case #{0}: {1}".format(i+1, solve(graph))






