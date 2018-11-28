xwins = ["XXXX", "TXXX", "XTXX", "XXTX", "XXXT"]
owins = ["OOOO", "TOOO", "OTOO", "OOTO", "OOOT"]

def check(k):
    counter = 0;
    for i in k:
        if i in xwins:
            return "X won"
        elif i in owins:
            return "O won"
        elif '.' in i:
            counter += 1
    for j in range(4):
        if k[0][j]+k[1][j]+k[2][j]+k[3][j] in xwins:
            return "X won"
        elif k[0][j]+k[1][j]+k[2][j]+k[3][j] in owins:
            return "O won"
    if (k[0][0]+k[1][1]+k[2][2]+k[3][3] in xwins) or (k[0][3]+k[1][2]+k[2][1]+k[3][0] in xwins):
        return "X won"
    elif (k[0][0]+k[1][1]+k[2][2]+k[3][3] in owins) or (k[0][3]+k[1][2]+k[2][1]+k[3][0] in owins):
        return "O won"
    elif counter > 0:
        return "Game has not completed"
    else:
        return "Draw"
    
f = open(r'A-large.in', 'r')
g = open(r'outputA.out', 'w')
t = int(f.readline())
for i in range(1, t+1):
    g.write("Case #"+str(i)+": ")
    k = [f.readline().replace('\n', ''),
        f.readline().replace('\n', ''),
        f.readline().replace('\n', ''),
        f.readline().replace('\n', '')]
    res = check(k)
    g.write(res+"\n")
    f.readline()
f.close()
g.close()
    
