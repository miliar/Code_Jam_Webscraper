def main():
    t = int(raw_input())
    for _i in xrange(t):
        inp = [0 for _ in xrange(4)]
        a = ""
        while a == "":
            a = raw_input()
        inp[0] = a
        inp[1] = raw_input()
        inp[2] = raw_input()
        inp[3] = raw_input()
        #print inp
        #checking
        testX = (lambda x : x == 'X' or x == 'T')
        testO = (lambda x : x == 'O' or x == 'T')
        winX = False
        winO = False
        complete = True
        #checking for completion
        for i in xrange(4):
            if '.' in inp[i]:
                complete = False
        #row checking
        for i in xrange(4):
            if filter(testX, inp[i]) == inp[i]: winX = True
            if filter(testO, inp[i]) == inp[i]: winO = True
        #diagonal checking
        _diag = [[inp[i][i] for i in xrange(4)],[inp[i][3-i] for i in xrange(4)]]
        for _diag1 in _diag: 
            if filter(testX, _diag1) == _diag1: winX = True
            if filter(testO, _diag1) == _diag1: winO = True
        #Column checking
        transp = zip(*inp)
        for i in transp:
            if filter(testX, i) == i: winX = True
            if filter(testO, i) == i: winO = True
        print "Case #%d:" %(_i+1),
        if winX: print "X won"
        elif winO: print "O won"
        elif complete: print "Draw"
        else: print "Game has not completed"
if __name__ == "__main__":
    main()
