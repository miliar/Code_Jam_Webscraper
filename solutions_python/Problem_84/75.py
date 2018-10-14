import sys

T = int(sys.stdin.readline())

for _ in range(T):
    out = "Case #%d:" % (_ + 1)
    row, col = [ int( c)  for c in sys.stdin.readline().split(' ')]
    pic = []
    for __ in range(row):
        pic.append(list(sys.stdin.readline().strip()))
    stop = False
    for rowIndex in range(row):
        if stop:
            break
        for colIndex in range(col):
            if pic [rowIndex][colIndex] == '#':
                if rowIndex < row - 1 and colIndex < col - 1 and \
                    pic[rowIndex + 1][colIndex] == '#' and \
                    pic[rowIndex][colIndex+ 1] == '#' and \
                    pic[rowIndex + 1][colIndex + 1] == '#':
                    pic [rowIndex][colIndex] = '/'
                    pic[rowIndex + 1][colIndex + 1] = '/'
                    pic[rowIndex + 1][colIndex] = '\\'
                    pic[rowIndex][colIndex+ 1] = '\\'
                else:
                    stop = True
                    break
    print out
    if stop:
        print 'Impossible'
    else:
        for __ in range(row):
            print ''.join(pic[__])
                    # fail
