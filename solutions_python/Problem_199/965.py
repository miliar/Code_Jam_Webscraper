def solve(board, k):
    def flip(c):
        if c == '+':
            return '-'
        return '+'

    def use_flipper(i):
        for j in range(k):
            board[i + j] = flip(board[i + j])

    n = len(board)

    nb = 0
    for i in range(0, n - k + 1):
        if board[i] == '-':
            nb += 1
            use_flipper(i)

    for i in range(n - k + 1, n):
        if board[i] == '-':
            return "IMPOSSIBLE"

    return str(nb)


f = open("A-large.in", "r")
o = open("a.out", "w")

lines = f.readlines()
t = int(lines[0])

for i in range(t):
    case, k = lines[i+1].split()
    o.write("Case #%d: %s\n" % (i+1, solve(list(case), int(k))))