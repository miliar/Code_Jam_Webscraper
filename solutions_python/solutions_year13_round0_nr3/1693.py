ps = open("palindromicSquares.dat")
psList = []
for line in ps:
    psList.append(int(line))

file = open("ups")
T = int(file.readline())

hh = 1
for x in range(T):
    lin = file.readline()
    line = lin.split()
    A = int(line[0])
    B = int(line[1])
    
    count = 0
    
    for pSq in psList:
        if pSq >= A and pSq <= B:
            count+=1
                
    print "Case #" + str(hh) + ": " + str(count)
    hh+=1