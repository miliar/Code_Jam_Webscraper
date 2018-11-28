from itertools import groupby

T = int(raw_input())

for case in range(T):
    R, C, W = map(lambda x: int(x), raw_input().split())

    if W == C:
        turns = C
    elif W == 1:
        turns = R*C
    else:
        board = [0 for _ in range(R) for _ in range(C)]
        turns = 0
        x = 0
        # cheat
        while sum(board) < R*C:
            turns += 1
            board[x] = 1
            # movable areas
            groups = [list(g) for k, g in groupby(board) if k == 0]

            if any(len(g)>=W for g in groups):
                x = x + W
            else:
                break
        # hit
        turns += W - 1

    print 'Case #%d: %d' % (case+1, turns)