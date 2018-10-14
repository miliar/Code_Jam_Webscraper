def parse(file):
    l = open(file, "r").readlines()
    l = l[1:]
    ll = []
    for (i,r) in enumerate(l):
        r = r.strip()
        if i % 5 == 0:
            ll.append([r])
        elif i % 5 < 4:
            ll[-1].append(r)
    return ll

def solve_tc(tc):
    x, o, dot = ["X", "T"], ["O", "T"], ["."]
    xw, ow = False, False
    anyDot = False
    for i in range(4):
        allX = True
        allO = True
        for j in range(4):
            allX   = allX and (tc[i][j] in x)
            allO   = allO and (tc[i][j] in o)
            anyDot = anyDot or (tc[i][j] in dot)
        xw = xw or allX
        ow = ow or allO
    for j in range(4):
        allX = True
        allO = True
        for i in range(4):
            allX   = allX and (tc[i][j] in x)
            allO   = allO and (tc[i][j] in o)
        xw = xw or allX
        ow = ow or allO
    allX = True
    allO = True
    for i in range(4):
        allX = allX and (tc[i][i] in x)
        allO = allO and (tc[i][i] in o)
    xw = xw or allX
    ow = ow or allO
    allX = True
    allO = True
    for i in range(4):
        allX = allX and (tc[i][3-i] in x)
        allO = allO and (tc[i][3-i] in o)
    xw = xw or allX
    ow = ow or allO
    
    if xw and ow:
        return "Draw"
    elif xw:
        return "X won"
    elif ow:
        return "O won"
    elif not anyDot:
        return "Draw"
    else:
        return "Game has not completed"

def solve(filename):
    tcs = parse(filename)
    f = open("out", "w")
    for (i, tc) in enumerate(tcs):
        r = solve_tc(tc)
        f.write("Case #%d: %s\n" % (i+1, r))
    f.close()
