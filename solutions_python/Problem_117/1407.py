
def cutLawn(uncut, n, m, lawn):
    # print uncut
    # cut rows
    # cut row at max height of row
    for i in range(len(lawn)):
        setting = 1
        for sqre in lawn[i]:
            setting = max(setting, sqre)
        #print setting
        #print lawn[i]
        uncut[i] = [setting] * m
        #print uncut[i]
    # cut columns at max height
    for i in range(m):
        setting = 1
        for k in range(n):
            setting = max(setting, lawn[k][i])
            #print lawn[k][i]
        #print "\n"
        for j in range(n):
            uncut[j][i] = min(setting, uncut[j][i])
            #print uncut[j][i]
        #print "\n"
    #print uncut
    return uncut 

            

    


infile = open("B-large.in", "r")
outfile = open("outputb.txt", "w")

num_T = int(infile.readline())
count = 0

while count < num_T:
    count += 1
    message = "Case #%d: " % count
    N, M = [int(x) for x in infile.readline().strip().split()]
    lawn = []
    for i in range(N):
        redo = infile.readline().strip().split()
        redo = [int(x) for x in redo]
        lawn.append(redo)

    uncut = []
    row = [100] * M
    for i in range(N):
        uncut.append(row)
    #print lawn
    test = cutLawn(uncut, N, M, lawn)
    test = cutLawn(uncut, N, M, lawn)
    #print test
    message = "Case #%d: " % count
    if test == lawn:
        #print test, lawn
        message += "YES"
    else:
        message += "NO"
    outfile.write(message + "\n")
