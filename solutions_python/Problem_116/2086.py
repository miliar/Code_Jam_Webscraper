import sys

f = open("A-large.in", "r")
out = open("out.txt", "w")

n = int(f.readline().strip())

for i in range(n):
    rows = []
    for y in range(4):
        rows.append(f.readline().strip())
    f.readline() # blank line
    cols = [''.join([rows[x][y] for x in range(4)]) for y in range(4)]
    diags = [''.join([rows[x][x] for x in range(4)]), ''.join([rows[x][-x-1] for x in range(4)])]
    result = None
    empty = False
    for line in rows + cols + diags:
        x = 0
        o = 0
        t = 0
        for c in line:
            if c == "X":
                x += 1
            elif c == "O":
                o += 1
            elif c == "T":
                t += 1
            elif c == ".":
                empty = True
        if x == 4 or x == 3 and t == 1:
            result = "X won"
            break
        elif o == 4 or o == 3 and t == 1:
            result = "O won"
            break
    if result == None:
        if empty:
            result = "Game has not completed"
        else:
            result = "Draw"
    out.write("Case #{}: {}\n".format(i+1, result))
out.close()
