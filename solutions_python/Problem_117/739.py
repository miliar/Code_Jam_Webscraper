data = open(r"C:\Users\Eric\Desktop\data.txt")
trials = int(data.readline())
for trial_num in range(trials):
    rows,columns = data.readline().split()
    rows,columns = int(rows),int(columns)
    lawn = []
    for i in range(rows):
        lawn.append(map(lambda x: int(x),data.readline().split()))
    good = True
    for row in range(0, rows):
        for column in range(0, columns):
            value = lawn[row][column]
            goodrow = True
            goodcol = True
            for r in range(rows):
                if lawn[r][column] > value:
                    goodrow = False
            for c in range(columns):
                if lawn[row][c]>value:
                    goodcol = False
            if not goodrow and not goodcol:
                good = False
    print "Case #%d: %s"%(trial_num+1,'YES' if good else 'NO')
