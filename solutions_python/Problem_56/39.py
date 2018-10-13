#!/usr/bin/env python2.6

# Copyright Nate White, 2010

import optparse
import sys

def generate(options):
    import random
    # TODO Write sample input generator
    print options.generate
    for i in xrange(options.generate):
        A, B, C = (random.randint(1, 10 ** 50), random.randint(2, 1000),
                   random.randint(1, 10 ** 50))
        print A, B, C

def main():
    parser = optparse.OptionParser()
    parser.set_usage('%prog [options] <file>')
    parser.add_option("-d", "--debug", default=False,
        action="store_true", help="print progress messages to stdout")
    parser.add_option("-g", "--generate", default=None, action="store",
        type="int", metavar="N", help="generate a sample input of N tests")
    parser.add_option("-p", "--profile", default=False, action="store_true",
        help="run with profiling enabled")
    parser.add_option("-v", "--verify", default=False, action="store_true",
        help="verify result using brute force algorithm")
    (options, args) = parser.parse_args()
    if len(args) != 0:
        print parser.error('Unexpected positional arguments seen')

    if options.generate:
        generate(options)
        return

    if options.profile:
        import cProfile as profile
        profile.runctx("puzzle(options, args)", globals(), locals())
    else:
        puzzle(options, args)

def brute(options, n):
    return 0 # TODO Write brute-force solver

def solve(options, n):
    return 0 # TODO Write production solver

def show(board):
    for y in xrange(len(board)):
        row = board[y]
        for x in xrange(len(row)):
            if row[x] is None:
                print ".",
            else:
                print row[x],
        print

def rotate(board, clockwise):
    for y in xrange(len(board)):
        row = board[y]
        new = [i for i in row if i is not None]
        cnt = len(new)
        if clockwise:
            board[y] = [None] * (len(board) - cnt) + new
        else:
            board[y] = new + [None] * (len(board) - cnt)

def rotate2(board):
    N = len(board)
    new = [None] * len(board)
    for y in xrange(len(board)):
        new[y] = [None] * len(board)
        for x in xrange(len(board)):
            new[y][x] = board[N - x - 1][y]
    return new

def gravity(board):
    N = len(board)
    new = [None] * len(board)
    for y in xrange(len(board)):
        new[y] = [None] * len(board)

    for x in xrange(N):
        column = [None] * len(board)
        for y in xrange(N):
            column[y] = board[y][x]
        column = [i for i in column if i is not None]
        column = [None] * (N - len(column)) + column
        for y in xrange(N):
            new[y][x] = column[y]
    return new

def search(board, K):
    N = len(board)
    win = [False, False]

    # Check horizontal
    for y in xrange(N):
        for x in xrange(N - K + 1):
            first = board[y][x]
            good = True
            if first is None or win[first]:
                continue
            for i in xrange(1, K):
                if board[y][x + i] != first:
                    good = False
                    break
            if good:
                win[first] = True
                if win[0] and win[1]:
                    return win

    # Check vertical
    for x in xrange(N):
        for y in xrange(N - K + 1):
            first = board[y][x]
            good = True
            if first is None or win[first]:
                continue
            for i in xrange(1, K):
                if board[y + i][x] != first:
                    good = False
                    break
            if good:
                win[first] = True
                if win[0] and win[1]:
                    return win

    # Check diagonal down-right
    for y in xrange(N - K + 1):
        for x in xrange(N - K + 1):
            first = board[y][x]
            good = True
            if first is None or win[first]:
                continue
            for i in xrange(1, K):
                if board[y + i][x + i] != first:
                    good = False
                    break
            if good:
                win[first] = True
                if win[0] and win[1]:
                    return win

    # Check diagonal down-left
    for y in xrange(N - K + 1):
        for x in xrange(K - 1, N):
            first = board[y][x]
            good = True
            if first is None or win[first]:
                continue
            for i in xrange(1, K):
                if board[y + i][x - i] != first:
                    good = False
                    break
            if good:
                win[first] = True
                if win[0] and win[1]:
                    return win

    return win

def puzzle(options, args):
    (T,) = ([int(i) for i in sys.stdin.readline().split()])
    for t in xrange(1, T + 1):
        # Parse input
        (N, K) = ([int(i) for i in sys.stdin.readline().split()])
        board = [None] * N
        for i in xrange(N):
            board[i] = [None] * N
            row = sys.stdin.readline()
            for j in xrange(N):
                if row[j] == 'R':
                    board[i][j] = 1
                elif row[j] == 'B':
                    board[i][j] = 0
                else:
                    assert row[j] == '.'
        #print search(board, K)
        #return

        if options.debug:
            print "Input!!"
            show(board)

        board = rotate2(board)
        if options.debug:
            print "Rotate"
            show(board)

        board = gravity(board)
        if options.debug:
            print "Gravity"
            show(board)

        res = search(board, K)
        if res == [False, False]:
            s = "Neither"
        elif res == [True, False]:
            s = "Blue"
        elif res == [False, True]:
            s = "Red"
        elif res == [True, True]:
            s = "Both"

        #res = solve(options, n)
        if options.verify:
            res2 = brute(options, n)
            if options.debug:
                print "Production solution", res, "vs. brute-force", res2
            assert res == res2
        print 'Case #%d: %s' % (t, s)

if __name__ == '__main__':
    main()
