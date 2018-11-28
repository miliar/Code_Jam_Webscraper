def tomek(table):
#    print table
    row = [0 for a in range(4)]
    col = [0 for a in range(4)]
    left = 0
    right = 0
    for i in range(4):        
        for j in range(4):
            row[i] += table[i][j]
            col[j] += table[i][j]
            if i == j:
                left += table[i][j]
            elif i+j == 3:
                right += table[i][j]
#    print row, col
    for i in range(4):
        if row[i] >= 7 or col[i] >= 7:
            return "O won"
        elif 0 <= row[i] <= 1 or 0 <= col[i] <= 1:
            return "X won"
    if left >= 7 or right >= 7:
        return "O won"
    elif 0 <= left <= 1 or 0 <= right <= 1:
        return "X won"
    else:
        return "Draw"

f = open("A-large.in", "r")
out = open("A-large.out", "w")
line = f.readline()
T = int(line)
table = [[0 for col in range(4)] for row in range(4)]
for i in range(0, T):
    mark = False
    for j in range(4):
        line = f.readline()
        for k in range(len(line[:-1])):
            ch = line[k]
            if ch == "O":
                table[j][k] = 2
            elif ch == "X":
                table[j][k] = 0
            elif ch == "T":
                table[j][k] = 1
            elif ch == ".":
                table[j][k] = -10
                mark = True
    result = tomek(table)
    line = f.readline()
    if mark and result == "Draw":
        result = "Game has not completed"
#    print "Case #%d: %s" %(i+1, result)
    out.write("Case #%d: %s\n" %(i+1, result))
f.close()
out.close()
