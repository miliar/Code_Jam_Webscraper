lines = open("large.in").read().split("\n")[1:]
if lines[-1] == "":
    lines.pop()

inside = 0
boards = []

for line in lines:
    if inside > 0 and inside <= height:
        boards[-1].append(map(int, line.split(" ")))
        inside += 1
    else:
        height, width = map(int, line.split(" "))
        inside = 1
        boards.append([])

for i, board in enumerate(boards):
    works = "YES"
    hirow = [max(board[y]) for y in range(len(board))]
    hicol = [max([board[y][x] for y in range(len(board))]) for x in
            range(len(board[0]))]

    for y in range(len(board)):
        for x in range(len(board[0])):
            if hirow[y] != board[y][x] and hicol[x] != board[y][x]:
                works = "NO"
    print "Case #%d: %s" % (i+1, works)
