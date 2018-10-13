for t in xrange(input()):
    board = {}

    # input -> board = {(n, m): a}
    isfinish = True
    for line_n in xrange(4):
        temp = [each_letter for each_letter in raw_input().rstrip()]
        if isfinish and '.' in temp:
            isfinish = False
        for m in xrange(4):
            board[(line_n, m)] =  temp[m]
    raw_input()

    # test each letter in the first line
    statu = None
    count = 0
    for (n,m) in [(n,m) for n in xrange(4) for m in xrange(4)]:
        symbol = board[(n,m)]
        #print "|\nthe %d symbol is %s."%(m+1,symbol)
        if symbol == '.':
            continue
        # test four different direction, right, down-right, down, down-left
        for direction in [(0,1),(1,1),(1,0),(1,-1)]:
            #print "|  direction is ", direction
            next_sym_idx = (n,m)
            count = 1
            # test if it has four same symbols adjoined
            for j in xrange(3):
                next_sym_idx = (next_sym_idx[0] + direction[0], next_sym_idx[1] + direction[1])
                #print "|    the next symbol is", next_sym_idx[0],",",next_sym_idx[1]
                if min(next_sym_idx) < 0 or max(next_sym_idx) > 3:
                    #print "|    out range!"
                    break
                elif board[next_sym_idx] == symbol or board[next_sym_idx] == 'T':
                    #print "|    OK, count is ",count+1
                    count += 1
                    statu = symbol
                else:
                    #print "|    Not the same!"
                    statu = None
                    break
            if count == 4:
                #print "|  Found!"
                break
        if count == 4:
            break

    # print reslut
    print "Case #%d:"%(t+1),
    if count == 4:
        print statu, "won"
    elif isfinish == True:
        print "Draw"
    else:
        print "Game has not completed"
