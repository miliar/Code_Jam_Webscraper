import sys
import math

def solve(bact):
    cnt = 0;
    while True:
        ok = False
        for x in range(100):
            for y in range(100):
                if bact[x][y]:
                    ok = True
                    break
            if ok:
                break
        if not ok:
            return cnt
        next = [[False]*100 for i in range(100)]
        for x in range(100):
            for y in range(100):
                if bact[x][y]:
                    if x>0 and bact[x-1][y] or y>0 and bact[x][y-1]:
                        next[x][y] = True
                else:
                    if x>=0 and bact[x-1][y] and y>0 and bact[x][y-1]:
                        next[x][y] = True
        bact = next
        cnt += 1

def do_test(input):
    line = input.readline().strip(' \r\n\t').split()
    M = int(line[0])
    bact = [[False]*100 for i in range(100)]
    for i in range(M):
        line = input.readline().strip(' \r\n\t').split()
        x1,y1,x2,y2 = (int(tt) for tt in line)
        for x in range(x1-1, x2):
            for y in range(y1-1, y2):
                bact[x][y] = True
    res = solve(bact)
    return str(res)

input = sys.stdin

N = int(input.readline())

for test in range(N):
    answer = do_test(input)
    print 'Case #%d: %s' % (test+1, answer)
    sys.stdout.flush()

        
