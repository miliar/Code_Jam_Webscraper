def process(fname):
    lines = readfile(fname + '.in')
    fout = open(fname + '.out', 'w')
    run(lines, fout)

def readfile(fname):
    fin = open(fname)
    rawlines = fin.readlines()
    lines = []
    for rawline in rawlines:
        lines.append(rawline.strip('\n'))
    return lines

def run(lines, fout):
    t = int(lines[0])
    
    for i in range(t):
        fout.write("Case #" + str(i+1) + ": " + checkboard(lines, i*5+1) + '\n')

def checkboard(lines, s):
    # for i in range(s, s+4):
    #     print(lines[i])
    for i in range(s, s+4):
        match = lines[i][0] != '.'
        for j in range(3):
            if lines[i][j] == lines[i][j+1] != '.':
                # print(lines[i][j] + ' == ' + lines[i][j+1])
                continue
            if lines[i][j] == 'T' or lines[i][j+1] == 'T':
                # print(lines[i][j] + ' == ' + lines[i][j+1])
                continue
            # print(lines[i][j] + ' != ' + lines[i][j+1])
            match = False
        if match:
            return(lines[i][0] + " won")
    for j in range(4):
        match = True
        for i in range(s,s+3):
            if lines[i][j] == lines[i+1][j] != '.':
                continue
            if lines[i][j] == 'T' or lines[i+1][j] == 'T':
                continue
            match = False
        if match:
                return(lines[s][j] + " won")
    match1 = True
    match2 = True
    for i in range(3):
        if lines[s+i][i] == lines[s+i+1][i+1] != '.':
            continue
        if lines[s+i][i] == 'T' or lines[s+i+1][i+1] == 'T':
            continue
        match1 = False

    for i in range(3):
        if lines[s+i][3-i] == lines[s+i+1][3-i-1] != '.':
            continue
        if lines[s+i][3-1] == 'T' or lines[s+i+1][3-i-1] == 'T':
            continue
        match2 = False
    if match1:
        return(lines[s][0] + ' won')
    if match2:
        return(lines[s][3] + ' won')
    incomplete = False
    for i in range(3):
        incomplete = ('.' in lines[s+i]) or incomplete
    if incomplete:
        return "Game has not completed"
    return "Draw"
