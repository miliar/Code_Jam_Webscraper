from Queue import *

def solve(board, k):
    closed = {}
    opens = Queue()
    opens.put((board, 0))

    while not opens.empty():
        state, steps = opens.get()
        if state in closed: continue
        if solved(state): return steps

        closed[state] = True
        for start in xrange(len(board) - k + 1):
            opens.put((flip(state, start, k), steps + 1))

    return 'IMPOSSIBLE'

def flip(board, start, k):
    board = list(board)
    for i in xrange(start, start+k):
        if board[i] == '+': board[i] = '-'
        else:               board[i] = '+'
    return ''.join(board)

def solved(board): return len(set(board)) == 1 and board[0] == '+'

if __name__ == '__main__':
    trials = int(raw_input())
    for case in xrange(trials):
        board, k = raw_input().split()
        soln = solve(board, int(k))

        print 'Case #%d: %s' % (case+1, str(soln))
