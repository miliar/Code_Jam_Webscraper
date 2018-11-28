def integerize(char):
    if char == 'X':
        return 1
    if char == 'O':
        return 10
    if char == '.':
        return -1000
    if char == 'T':
        return 0

def test(board, n, nCase):
    sums = [0 for i in range(n+n+2)]
    tsum = 0
    for i in range(n):
        for j in range(n):
            sums[i] += board[i][j]
            sums[n + j] += board[i][j]
            if i == j:
                sums[n + n] += board[i][j]
            if (i + j == n - 1):
                sums[n + n + 1] += board[i][j]
            tsum += board[i][j]
    print 'Case #' + str(nCase) + ':',
    for i in range(len(sums)):
        if sums[i] == 3 or sums[i] == 4:
            print 'X won'
            break
        if sums[i] == 30 or sums[i] == 40:
            print 'O won'
            break
    else:
        if tsum < -800:
            print 'Game has not completed'
        else:
            print 'Draw'

if __name__ == '__main__':
    t = int(raw_input())
    n = 4
    for i in range(t):
        test([[integerize(char) for char in raw_input()] for j in range(n)], n, i + 1)
        raw_input()

