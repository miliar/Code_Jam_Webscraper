T = input()
other = lambda x: "B" if x == "O" else "O"
for i in xrange(T):
    line = raw_input().split()
    N = int(line[0])
    C = zip(line[1::2], map(int, line[2::2]))
    C_col = {"B": [c for c in C if c[0] == "B"], "O": [c for c in C if c[0] == "O"]}
    #print C
    #print C_col
    moves = 0
    pos = {"B" : 1, "O" : 1}
    while len(C) != 0:
        cur = C.pop(0)
        cur_c = cur[0]
        del C_col[cur_c][0]
        oth_c = other(cur_c)
        oth = C_col[oth_c]
        if len(oth) != 0:
            oth = oth[0]
        pressed = False
        while pos[cur_c] != cur[1] or not pressed:
            if pos[cur_c] == cur[1]:
                pressed = True
            else:
                pos[cur_c] += cmp (cur[1], pos[cur_c])
            if len(oth) != 0:
                #print oth, pos[oth_c], oth_c
                pos[oth_c] += cmp (oth[1], pos[oth_c])
            moves += 1
        
    print "Case #%d: %d" % (i + 1, moves)