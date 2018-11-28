from collections import deque
fin = open("A-large.in")
fout = open("A-large.out", "wt")
testCnt = int(fin.readline())

class RobotMove:
    name = ""
    targe = 0
    def __init__(self, name, target):
        self.name = name
        self.target = target
        
for testCase in range(0, testCnt):
    strItems = fin.readline().strip().split(" ")
    itemCnt = int(strItems[0])

    robotMoves = []
    for i in range (0, itemCnt):
        name = strItems[1+i*2]
        target = int(strItems[2+i*2])
        robotMoves.append(RobotMove(name, target))
    
    # Build robot queues
    queues = {"O":deque([]), "B":deque([])}
    for move in robotMoves:
        queues[move.name].append(move)

    pos = {"O":1, "B":1}
    totalTime = 0
    for move in robotMoves:
        pusherRobot = move.name
        otherRobot = "O"
        if pusherRobot=="O":
            otherRobot = "B"

        elapsed = abs(pos[pusherRobot]-move.target)+1
        pos[pusherRobot]=move.target
        queues[pusherRobot].popleft()
        totalTime+=elapsed

        # for other robot:
        otherQueue = queues[otherRobot]
        if len(otherQueue)>0:
            if pos[otherRobot]<otherQueue[0].target:
                pos[otherRobot] = min(pos[otherRobot]+elapsed, otherQueue[0].target)
            else:
                pos[otherRobot] = max(pos[otherRobot]-elapsed, otherQueue[0].target)
            # don't pop from other robots queue

    string = "Case #%d: %d\n" % (testCase+1, totalTime)
    print string
    fout.write(string)

print "OK"
fin.close()    
fout.close()
