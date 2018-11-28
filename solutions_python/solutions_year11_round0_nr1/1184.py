from collections import deque
import sys

def solve2(commands, commandsByR):
    totalTime = 0
    pos = [1, 1]
    byRIdx = [0, 0]
    while commands:
        c = commands.popleft()
        ci = c[0]
        byRIdx[ci] += 1
        oi = 0 if ci else 1
        moveTime = abs(c[1] - pos[ci])
        totalTime += moveTime + 1
        pos[ci] = c[1]
        if byRIdx[oi] < len(commandsByR[oi]):
            oc = commandsByR[oi][byRIdx[oi]]
            od = oc[1] - pos[oi]
            if abs(od) > 0:
                reqMT = (moveTime + 1) if abs(od) > (moveTime + 1) else abs(od)
                pos[oi] = pos[oi] + ((od/abs(od)) * reqMT)
    return totalTime
        
        
    

def solve(line):
    sp = line.split()
#    print sp
    n = int(sp[0])
    cn = 0
    commands = deque()
    commandByR = [[],[]]
    for i in range(1, n * 2, 2):
        r = 0 if sp[i] == 'O' else 1
        b = int(sp[i + 1])
        c = [r, b, cn]
        cn += 1
        commands.append(c)
        commandByR[r].append(c)
#    print commands
#    print commandByR
    return solve2(commands, commandByR)
    
        
        
    

def main():
    f = open(sys.argv[1], 'r')
    lines = f.read().splitlines()
    N = int(lines[0])
    for i in range(1, N + 1):
        t = solve(lines[i])
        print "Case #%d: %d" % (i, t)
    
    
    
if __name__ == '__main__':
    main()