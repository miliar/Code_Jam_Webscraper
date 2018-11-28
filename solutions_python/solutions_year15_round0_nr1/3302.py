fh = open("A-large.in", "r")

t = int(fh.readline())

for i in range(0,t):
    line = fh.readline().strip()
    testcase = line.split()
    max = int(testcase[0])
    aud = [int(x) for x in testcase[1]]
    ans = 0
    curr_ovations = 0
    j = 0
    
    while j < max:
        curr_ovations = curr_ovations + aud[j] #num ovations

        if curr_ovations < j+1: 
            ans = ans + (j+1 - curr_ovations)
            curr_ovations = curr_ovations + (j+1 - curr_ovations)
        
        j = j+1

    print("Case #%d: %d" % (i+1,ans))

fh.close()
