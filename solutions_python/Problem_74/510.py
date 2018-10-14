inFile = open("A-large.in.in", 'r')
outFile = open("botTrust.out",'w')
N = int(inFile.readline())

for i in range(1,N+1):
    line = inFile.readline().split()
    M = int(line[0])
    opos = 1
    bpos = 1
    otime = 0
    btime = 0
    tottime = 0
    for j in range(M):
        bot = line[2*j+1]
        dest = int(line[2*j+2])
        if bot == 'O':
            dist = abs(dest - opos)
            tottime = max(tottime+1, otime+dist+1)
            otime = tottime
            opos = dest
        elif bot == 'B':
            dist = abs(dest - bpos)
            tottime = max(tottime+1, btime+dist+1)
            btime = tottime
            bpos = dest
    outFile.write("Case #"+str(i)+": "+str(tottime)+"\n")
    print("Case #"+str(i)+": "+str(tottime))
