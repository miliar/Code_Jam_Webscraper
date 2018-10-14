def xl(l):
    return xrange(len(l))

def moveright(s):
    new="".join([x for x in s if x in ["B","R"]])
    return "."*(len(s)-len(new))+new

debug=False
for case in range(input()):
    print "Case #"+str(case+1)+":",
    N,K=map(int,raw_input().split())
    board=[]
    for i in xrange(N):
        board.append(moveright(raw_input()))
    if debug:print "\n".join(board)
    if K>N:
        print "Neither"
        continue
    redwin=False
    bluewin=False
    for i in xrange(N):
     for j in xrange(N):
       for di,dj in [(0,1),(1,0),(1,1),(1,-1)]:
        try:
            if all(board[i+di*d][j+dj*d]=="R" for d in xrange(K)):
                redwin=True
            if all(board[i+di*d][j+dj*d]=="B" for d in xrange(K)):
                bluewin=True
        except:
            pass
    if debug: print redwin,bluewin
    if redwin and bluewin:
        print "Both"
    elif redwin:
        print "Red"
    elif bluewin:
        print "Blue"
    else:
        print "Neither"
