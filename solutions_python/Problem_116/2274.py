def whoWon(mesh):
    # horizontal
    for i in xrange(4):
        cx, co, ct = 0, 0, 0
        for j in xrange(4):
            if mesh[i * 4 + j] in ['X']: cx += 1
            if mesh[i * 4 + j] in ['O']: co += 1
            if mesh[i * 4 + j] in ['T']: ct += 1
        if cx == 4: return 'X'
        elif co == 4: return 'O'
    	elif cx == 3 and ct == 1: return 'X'
    	elif co ==3 and ct == 1: return 'O'
    # vertical
    for i in xrange(4):
        cx, co, ct = 0, 0, 0
        for j in xrange(4):
            if mesh[i + j*4] in ['X']: cx += 1
            if mesh[i + j*4] in ['O']: co += 1
            if mesh[i + j*4] in ['T']: ct += 1
        if cx == 4: return 'X'
        elif co == 4: return 'O'
    	elif cx == 3 and ct == 1: return 'X'
    	elif co ==3 and ct == 1: return 'O'
    # right diagonal
    cx, co, ct = 0, 0, 0
    for i in [0, 5, 10, 15]:
        if mesh[i] in ['X']: cx += 1
        if mesh[i] in ['O']: co += 1
        if mesh[i] in ['T']: ct += 1
    if cx == 4: return 'X'
    elif co == 4: return 'O'
    elif cx == 3 and ct == 1: return 'X'
    elif co ==3 and ct == 1: return 'O'
    # left diagonal
    cx, co, ct = 0, 0, 0
    for i in [3, 6, 9, 12]:
        if mesh[i] in ['X']: cx += 1
        if mesh[i] in ['O']: co += 1
        if mesh[i] in ['T']: ct += 1
    if cx == 4: return 'X'
    elif co == 4: return 'O'
    elif cx == 3 and ct == 1: return 'X'
    elif co ==3 and ct == 1: return 'O'
    #print co, cx
    fc = 0
    for c in mesh: fc = fc + 1 if c in "OXT" else 0
    if fc == 16: return 0
    return 1  # Nobody have won 

t = int(raw_input())
for i in xrange(1, t+1):
	board = ""
	for j in xrange(4):
		l = raw_input() 
		board += l
	
	ww = whoWon(board)
	if ww == 0: print "Case #"+str(i)+": Draw"
	elif ww == 1: print "Case #"+str(i)+": Game has not completed"
	else: print "Case #"+str(i)+": " + str(ww) + " won"
	raw_input()