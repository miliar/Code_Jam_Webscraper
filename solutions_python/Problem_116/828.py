T = int(raw_input())
for t in range(1, T + 1):
    lines = []
    while(len(lines) < 4):
        line = raw_input()
        if line != '':
            lines.append(line)
    hor = '#'
    hor += '#'.join(lines)
    hor += '#'
    for c in range(4):
        for r in range(4):
            hor += lines[r][c]
        hor += '#'
    for i in range(4):
        hor += lines[i][i]
    hor += '#'
    for i in range(4):
        hor += lines[i][3 - i]
    hor += '#'

    import re
    o = []
    o.append(re.compile("#OOOO#"))
    for i in range(4):
        post = ['O' for j in range(3 - i)]
        prefix = ['O' for j in range(i)]
        prefix = '#' + ''.join(prefix)
        post = ''.join(post) + '#'
        o.append(re.compile(prefix + 'T' + post))
    

    x = []
    x.append(re.compile("#XXXX#"))
    for i in range(4):
        post = ['X' for j in range(3 - i)]
        prefix = ['X' for j in range(i)]
        prefix = '#' + ''.join(prefix)
        post = ''.join(post) + '#'
        x.append(re.compile(prefix + 'T' + post))
    
    print "Case #%d:" % t,
    owon = False
    for owin in o:
        r = owin.search(hor)
        if r:
            owon = True
            print "O won"
            break
    if owon:
        continue

    xwon = False
    for xwin in x:
        r = xwin.search(hor)
        if r:
            xwon = True
            print "X won"
            break
    if xwon:
        continue
    
    if hor.find('.') != -1:
        print "Game has not completed"
        continue
    
    print "Draw"

