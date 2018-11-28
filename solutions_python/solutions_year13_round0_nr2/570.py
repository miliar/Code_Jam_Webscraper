inputfile = file("B-large.in", "rb")
outputfile = file("B-large.out", "wb")
out_yes = "Case #%d: YES"
out_no = "Case #%d: NO"
parse_line = lambda: [int(a) for a in inputfile.readline().split()]

def snip_nl(s):
    if s.endswith("\r\n"):
        return s[:-2]
    if s.endswith("\n"):
        return s[:-1]
    return s


T = int(inputfile.readline())
for ncase in xrange(1,T+1):
    N, M = parse_line()
    max_rows = [0]*N
    max_cols = [0]*M
    board = []
    case_out = False
    for i in xrange(N):
        board.append(parse_line())

    # Build row and col maximums
    for i in xrange(N):
        for j in xrange(M):
            max_rows[i] = max(max_rows[i], board[i][j])
            max_cols[j] = max(max_cols[j], board[i][j])
    import pprint

    for i in xrange(N):
        if case_out:
            break
        for j in xrange(M):
            if board[i][j] < max_rows[i] and board[i][j] < max_cols[j]:
                case_out = True
                break
    if case_out:
        print >>outputfile, out_no % ncase
    else:
        print >>outputfile, out_yes % ncase
