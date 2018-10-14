import sys
import math

def Problem3(num, n, k):
    divs = pow(2, math.floor(math.log(k, 2)))
    stallsLeftBefore = math.ceil((n - k + 1) / divs)
    stallsLeftAfter = stallsLeftBefore - 1
    
    print("Case #" + str(num) + ": " + str(math.ceil(stallsLeftAfter/2)) + " " + str(math.floor(stallsLeftAfter/2)))
            


cnt = 0
numCases = 0
for line in sys.stdin:
    if cnt == 0:
        numCases = int(line)
    else:
        if cnt <= numCases:
            split = line.split()
            Problem3(cnt, int(split[0]), int(split[1]))
        else:
            break
        
    cnt = cnt + 1


    
