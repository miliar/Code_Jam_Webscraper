import sys

dr = [0, 1, 1, 1]
dc = [1, 1, -1, 0]

def generate(board, K):
    res = set()
    N = len(board)

    for r in xrange(N):
        for c in xrange(N):
            for d in xrange(len(dc)):
                curr_row = r
                curr_col = c
                curr_string = ""

                for l in xrange(K):
                    curr_string += board[curr_row][curr_col]
                    curr_row += dr[d]
                    curr_col += dc[d]
                    if curr_row >= N or curr_row < 0 or curr_col >= N or curr_col < 0:
                        break

                res.add(curr_string)

    return res

def winner(board, K):
    all_strings = generate(board, K)

    red =  K * 'R'
    blue =  K * 'B'
    
    red_wins = red in all_strings
    blue_wins = blue in all_strings

    if red_wins and blue_wins:
        return "Both"
    if red_wins:
        return "Red"
    if blue_wins:
        return "Blue"
    return "Neither"

def rotate_right(row):
    new_row = filter(lambda r: r is not '.', row)

    while len(new_row) < len(row):
        new_row = '.' + new_row

    return new_row

def gravity(board):
    return map(rotate_right, board)

def rotate(board):
    return zip(*board[::-1])

def solve(board, K):
    return winner(rotate(gravity(board)), K)

T = int(raw_input())

for t in xrange(T):
    N, K = map(int, sys.stdin.readline().split(' '))
    board = [sys.stdin.readline().strip('\n') for i in xrange(N)]

    print 'Case #%d: %s' % (t+1, solve(board, K))
