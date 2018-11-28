import sys

def Problem1(num, d, n, horses):
    slowestTime = 0
    for h in horses:
        distanceLeft = d - h[0]
        timeLeft = distanceLeft / h[1]
        if slowestTime == 0 or timeLeft > slowestTime: slowestTime = timeLeft
    
    speed = d / slowestTime
    print("Case #" + str(num) + ": " + str(speed))
            

line = sys.stdin.readline()
numCases = int(line)
curCase = 0

while True:
    line = sys.stdin.readline()
    if not line:
        break
    
    curCase = curCase + 1
    split = line.split()
    
    d = split[0]
    n = split[1]
    horses = []
    
    for i in range(0, int(n)):
        line = sys.stdin.readline()
        split2 = line.split()
        horses.append((int(split2[0]), int(split2[1])))
    
    Problem1(curCase, int(d), int(n), horses)
    
