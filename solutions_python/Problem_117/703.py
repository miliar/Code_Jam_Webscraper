f = open("inputblarge.txt")
cases = int(f.readline())

for c1 in range(0,cases):
    lawn = []
    line = f.readline().split(" ")
    r = int(line[0])
    c = int(line[1])
    good = []
    for i in range(0,r):
        lawn.append([])
        good.append([])
        l = f.readline()
        l = l.split(" ");
        for j in l:
            good[i].append(False)
            lawn[i].append(int(j))
    for i in range(0,len(lawn)):
        m = 0
        for j in range(0,len(lawn[i])):
            if lawn[i][j] > m:
                m=lawn[i][j]
        for j in range(0,len(lawn[i])):
            if lawn[i][j] == m:
                good[i][j] = True
    for j in range(0,len(lawn[0])):
        m = 0
        for i in range(0,len(lawn)):
            if lawn[i][j] > m:
                m=lawn[i][j]
        for i in range(0,len(lawn)):
            if lawn[i][j] == m:
                good[i][j] = True
    g = True
    for i in good:
        for j in i:
            if j == False:
                g = False
    if g:
        print "Case #"+str(c1+1)+": YES"
    else:
        print "Case #"+str(c1+1)+": NO"
