def check_win(l,r):
    if l.count('X') == 4 or (l.count('X') == 3 and l.count('T') == 1):
        r = "X won"
    if l.count('O') == 4 or (l.count('O') == 3 and l.count('T') == 1):
        r = "O won"
    if '.' in l and r =="":
        r =  "Game has not completed"
    return r    
fin = open("A-large.in","r")
fout = open("A-large.out","w")
t = int(fin.readline())
for i in range(1,t + 1):
    r = ""
    b = []
    for j in range(0,4):
        l = fin.readline().strip()
        r = check_win(l,r)          
        b.append(l)    
    for j in range(0,4):
        l = ""
        for k in range(0,4):
            l = l + b[k][j]
        r = check_win(l,r)
    l = b[0][0] + b[1][1] + b [2][2] + b[3][3]
    r = check_win(l,r)
    l = b[0][3] + b[1][2] + b [2][1] + b[3][0]
    r = check_win(l,r)
    if r == "":
        r = "Draw"
    fout.write("Case #%d: %s\n" % (i,r))
    fin.readline()
fin.close()
fout.close()
