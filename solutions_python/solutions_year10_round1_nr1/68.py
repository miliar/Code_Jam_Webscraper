def who_wins(board, k):
    rwins = False
    bwins = False
    for i in range(len(board)):
        max_r = 0
        max_b = 0
        
        for j in range(len(board)):
            item = board[i][j]
            if item == 'R':
                max_r += 1
                if max_r == k:
                    rwins = True
            else:
                max_r = 0
            if item == 'B':
                max_b += 1
                if max_b == k:
                    bwins = True
            else:
                max_b = 0

    for i in range(len(board)):
        max_r = 0
        max_b = 0
        for j in range(len(board)):
            item = board[j][i]
            
            if item == 'R':
                max_r += 1
                if max_r == k:
                    rwins = True
            else:
                max_r = 0
            if item == 'B':
                max_b += 1
                if max_b == k:
                    bwins = True
            else:
                max_b = 0

    max_r = 0
    max_b = 0
    l = len(board)
    for i in range(l):
        max_r = 0
        max_b = 0
        for j in range(i+1):
            item = board[l-j-1][l-i+j-1]
            if item == 'R':
                max_r += 1
                if max_r == k:
                    rwins = True
            else:
                max_r = 0
            if item == 'B':
                max_b += 1
                if max_b == k:
                    bwins = True
            else:
                max_b = 0


    max_r = 0
    max_b = 0
    l = len(board)
    for i in range(l):
        max_r = 0
        max_b = 0
        for j in range(i+1):
            item = board[i-j][j]
            if item == 'R':
                max_r += 1
                if max_r == k:
                    rwins = True
            else:
                max_r = 0
            if item == 'B':
                max_b += 1
                if max_b == k:
                    bwins = True
            else:
                max_b = 0

    max_r = 0
    max_b = 0
    l = len(board)
    for i in range(l):
        max_r = 0
        max_b = 0
        for j in range(i+1):
            item = board[l-i-1+j][j]
            if item == 'R':
                max_r += 1
                if max_r == k:
                    rwins = True
            else:
                max_r = 0
            if item == 'B':
                max_b += 1
                if max_b == k:
                    bwins = True
            else:
                max_b = 0

    max_r = 0
    max_b = 0
    l = len(board)
    for i in range(l):
        max_r = 0
        max_b = 0
        for j in range(i+1):
            item = board[j][l-i-1+j]
            if item == 'R':
                max_r += 1
                if max_r == k:
                    rwins = True
            else:
                max_r = 0
            if item == 'B':
                max_b += 1
                if max_b == k:
                    bwins = True
            else:
                max_b = 0

    if not bwins and not rwins:
        return "Neither"
    if bwins:
        if rwins:
            return "Both"
        return "Blue"
    return "Red"


def gravity(board):
    import collections
    new_board = {}
    for i in range(len(board)):
        new_board[i] = collections.defaultdict(lambda : '.')
    for i in range(len(board)):
        row = len(board)-1
        for j in range(len(board)):
            if board[len(board)-i-1][len(board)-j-1] in ('R', 'B'):
                new_board[row][i] = board[len(board)-i-1][len(board)-j-1]
                row -= 1
    return new_board


if __name__ == "__main__":
    n = int(raw_input())
    for i in range(1, n+1):
        N, K = map(int, raw_input().split())
        board = []
        for j in range(N):
            board.append(raw_input())
        board = gravity(board)
        print "Case #%d: %s" % (i, who_wins(board, K))
