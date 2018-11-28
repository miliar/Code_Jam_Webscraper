file = open("lawnmowerData")
T = int(file.readline())

for yy in range(T):
    ffrl = file.readline().split()
    N = int(ffrl[0])
    M = int(ffrl[1])

    lawn = []
    for ilk in range(N):
        line = file.readline().replace('\n','')
        li = line.split()
        lawn.append(li)
    
    willWork = "YES"
    
    for i in range(N):
        for j in range(M):
            c = int(lawn[i][j])
            if c == 1:
                if '2' in lawn[i]:
                    for x in range(N):
                        if '2' in lawn[x][j]:
                            willWork = "NO"

    
    print "Case #" + str(yy+1) + ": " + willWork