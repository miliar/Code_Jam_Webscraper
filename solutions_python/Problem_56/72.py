#!/usr/bin/python

import sys, re

INPUT = sys.stdin
INPUT = open(sys.argv[1],'r')

def getline():
    return INPUT.readline()[:-1]

def trace(*strs):
    print >> sys.stderr, '..',
    for str in strs:
        print >> sys.stderr, str,
    print >> sys.stderr

def memoize(f):
    memos = {}
    def memoized_f( *args ):
        try:
            result = memos[args]
            trace(args, ": got result from memo")
        except KeyError:
            result = f(*args)
            trace(args, ": got result by calling")
            memos[args] = result
        return result
    return memoized_f

n_cases = int(getline())
trace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    trace()
    trace( 'Case #', case_num )

    (N,K) = map(int,getline().split())

    something = [ [' '] * N for i in range(N) ]
    row_ = []
    post_rotate_col_ = []
    for r in range(N):
        line = getline()
        assert len(line) == N
        row_.append(line)
        prc = re.sub(r'\.', '', line)
        post_rotate_col_.append(prc)
        n_dots = N - len(prc)
        for (i,char) in enumerate(prc):
            something[r][i+n_dots] = char

    # print row_
    # print post_rotate_col_
    # for r in range(N):
        # print something[r]

    R_has_K_in_a_row = False
    B_has_K_in_a_row = False

    # "horiz"
    for r in range(N):
        current_colour = None
        for c in range(N):
            colour = something[r][c]
            if colour == current_colour:
                n_of_current_colour += 1
                if n_of_current_colour >= K:
                    if colour == 'R':
                        R_has_K_in_a_row = True
                    elif colour == 'B':
                        B_has_K_in_a_row = True
            else:
                current_colour = colour
                n_of_current_colour = 1

    # "vert"
    for c in range(N):
        current_colour = None
        for r in range(N):
            colour = something[r][c]
            if colour == current_colour:
                n_of_current_colour += 1
                if n_of_current_colour >= K:
                    if colour == 'R':
                        R_has_K_in_a_row = True
                    elif colour == 'B':
                        B_has_K_in_a_row = True
            else:
                current_colour = colour
                n_of_current_colour = 1

    # diagonally: r+c == q
    for q in range(2*N):
        # print
        # print 'q:', q
        current_colour = None
        for r in range(N):
            c = q - r
            if 0 <= c < N:
                # print r, c
                colour = something[r][c]
                if colour == current_colour:
                    n_of_current_colour += 1
                    if n_of_current_colour >= K:
                        if colour == 'R':
                            R_has_K_in_a_row = True
                        elif colour == 'B':
                            B_has_K_in_a_row = True
                else:
                    current_colour = colour
                    n_of_current_colour = 1

    # diagonally: r-c == q
    for q in range(-N,+N):
        # print
        # print 'q:', q
        current_colour = None
        for r in range(N):
            c = r - q
            if 0 <= c < N:
                # print r, c
                colour = something[r][c]
                if colour == current_colour:
                    n_of_current_colour += 1
                    if n_of_current_colour >= K:
                        if colour == 'R':
                            R_has_K_in_a_row = True
                        elif colour == 'B':
                            B_has_K_in_a_row = True
                else:
                    current_colour = colour
                    n_of_current_colour = 1

    if R_has_K_in_a_row and B_has_K_in_a_row:
        answer = 'Both'
    elif R_has_K_in_a_row:
        answer = 'Red'
    elif B_has_K_in_a_row:
        answer = 'Blue'
    else:
        answer = 'Neither'

    print 'Case #%d: %s' % (case_num, answer)
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
