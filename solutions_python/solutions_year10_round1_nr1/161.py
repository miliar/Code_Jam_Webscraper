#!/usr/bin/python

DEBUG = 0

def move_right(line, N):
    trimmed = line.replace(".", "")
    moved = (N-len(trimmed)) * '.' + trimmed
    return moved

T = int(raw_input().strip())
for t in range(T):
    N, K = [int(x) for x in raw_input().split()]
    if DEBUG: print "%d^2 board, game of join-%d" % (N, K)
    board = []
    for n in range(N):
        board.append(raw_input().strip())
    if DEBUG: print board

    # now assume down is to the RIGHT
    # gravity
    board = [move_right(x, N) for x in board]
    if DEBUG: print board

    found_runs = {}
    def found(run):
        if run != '.' and DEBUG: print "found run of %s" % current_run
        found_runs[run] = 1

    # decide
    # look for diagonal-down runs
    if DEBUG: print "diag down"
    for y in range(-N, N):
        current_run = None
        current_run_length = 0
        for x in range(N):

            yy = y+x
            if yy<0 or yy>= N: continue

            c = board[yy][x]
            if current_run == c:
                current_run_length += 1
                if current_run_length >= K:
                    found(current_run)
            else:
                current_run = c
                current_run_length = 1
        
    # look for diagonal-up runs
    if DEBUG: print "diag up"
    for y in range(2*N):
        current_run = None
        current_run_length = 0
        for x in range(N):

            yy = y-x
            if yy<0 or yy>= N: continue
#            if DEBUG: print x,yy

            c = board[yy][x]
            if current_run == c:
                current_run_length += 1
                if current_run_length >= K:
                    found(current_run)
            else:
                current_run = c
                current_run_length = 1
#        if DEBUG: print

    # look for vertical runs
    if DEBUG: print "vert"
    for x in range(N):
        current_run = None
        current_run_length = 0
        for y in range(N):
            c = board[y][x]
            if current_run == c:
                current_run_length += 1
                if current_run_length >= K:
                    found(current_run)
            else:
                current_run = c
                current_run_length = 1

    # look for horizontal runs
    if DEBUG: print "horiz"
    for line in board:
        current_run = None
        current_run_length = 0
        for c in line:
            if current_run == c:
                current_run_length += 1
                if current_run_length >= K:
                    found(current_run)
            else:
                current_run = c
                current_run_length = 1

    if DEBUG: print "found runs:", found_runs
    if found_runs.get('R'):
        if found_runs.get('B'):
            decision = "Both"
        else:
            decision = "Red"
    elif found_runs.get('B'):
        decision = "Blue"
    else:
        decision = "Neither"
    print "Case #%d: %s" % (t+1, decision)
