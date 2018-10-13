import math

fi = open("input.in")
fo = open("output.out", "w+")

totalCaseNum = int(fi.readline())

for i in range(1, totalCaseNum + 1):
    temp = fi.readline()
    data = [j for j in map(int, fi.readline().split())]
    bestMinute = max(data)
    cutoffMinute = bestMinute
    
    while cutoffMinute > 1:
        cutoffMinute -= 1
        thisRoundMinute = cutoffMinute
        for j in data:
            if j > cutoffMinute:
                thisRoundMinute += math.ceil(j / cutoffMinute) - 1
                
        if thisRoundMinute <= bestMinute:
            bestMinute = thisRoundMinute
        
    fo.write("Case #%d: %d" % (i, bestMinute) + "\n")
    print(bestMinute)
