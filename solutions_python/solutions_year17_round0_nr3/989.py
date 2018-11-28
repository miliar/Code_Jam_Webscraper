import math

fr = open("input.in", 'r')
fw = open("output.txt", 'w')

lines = fr.readlines()

numTests = int(lines[0].strip())
curTest = 0
curLine = 1

def getLine():
    global curLine
    global lines
    curLine += 1
    return lines[curLine-1]
    
def solve(n, k, l, r):

    if k == 0:
        return l, r
        
    if n%2 == 1:
        n = math.floor(n/2)
        k -= 1
        maxN = n
        minN = n
    else:
        maxN = math.floor((n+1)/2)
        minN = maxN - 1
        k -= 1
        
    if k == 0:
        return maxN, minN
        
    if k%2 == 1:
        return solve(maxN, math.ceil(k/2), maxN, minN)
    else:
        return solve(minN, math.floor(k/2), maxN, minN)
    
while curTest < numTests:
    n, k = map(int, getLine().strip().split())
    
    maxN, minN = solve(n, k, 0, 0)
    fw.write("Case #%d: %d %d\n" % (curTest+1, maxN, minN))

    curTest += 1
                    
fr.close()
fw.close()