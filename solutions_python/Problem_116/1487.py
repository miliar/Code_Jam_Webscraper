cases = int(raw_input())

def check(*args):
    if args[0] == '.':
        return False
    if args[0] == 'T':
        if args[1] == args[2] == args[3] != '.':
            return args[1]
        else:
            return False
    else:
        def match(l):
            return l=='T' or l==args[0]
        if all(map(match, args)):
            return args[0]
        else:
            return False

for i in xrange(1, cases+1):
    board = []
    complete = True
    for _ in xrange(4):
        row = raw_input()
        if row[0]=='.' or row[1]=='.' or row[2]=='.' or row[3]=='.':
            complete = False
        board.append(row)
    assert (raw_input()=="")

    res = check(*(board[j][j] for j in xrange(4)))
    if not res:
        res = check(*(board[j][3-j] for j in xrange(4)))
    if res:
        print "Case #%d: %s won" %(i, res)
        continue

    flag = False
    for j in xrange(4):
        res = check(*board[j])
        if not res:
            res = check(board[0][j], board[1][j], board[2][j], board[3][j])
        if res:
            print "Case #%d: %s won" %(i, res)
            flag = True
            break

    if flag:
        continue
    if complete:
        print "Case #%d: Draw" %(i,)
    else:
        print "Case #%d: Game has not completed" %(i,)
