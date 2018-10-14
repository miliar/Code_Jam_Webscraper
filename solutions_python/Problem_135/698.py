import sys

T = int(sys.stdin.readline())

for case in range(0,T):
    config1 = []
    row1 = int(sys.stdin.readline()) - 1
    for i in range(0,4):
        row = map(int, sys.stdin.readline().strip().split())
        config1.append(row)
        
    config2 = []
    row2 = int(sys.stdin.readline()) - 1
    for i in range(0,4):
        row = map(int, sys.stdin.readline().strip().split())
        config2.append(row)
        
        
    #print config1[row1]
    #print config2[row2]
    
    common = []
    
    for i1 in range(0,4):
        for i2 in range(0,4):
            if (config1[row1][i1] == config2[row2][i2]):
                common.append(config1[row1][i1])
                
    if (len(common) == 1):
        print "Case #" + str(case+1) + ": " + str(common[0])
    elif (len(common) == 0):
        print "Case #" + str(case+1) + ": " + "Volunteer cheated!"
    else:
        print "Case #" + str(case+1) + ": " + "Bad magician!"
        