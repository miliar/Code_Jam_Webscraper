import sys
import math

def solve(buttons):
    pos = [1, 1]
    last_time = [0, 0]
    elapsed = 0
    for rob, but in buttons:
        p0 = pos[rob]
        dt = elapsed - last_time[rob]
        dx = abs(p0-but)
        dx -= dt
        if dx<0:
            dx = 0
        elapsed += dx + 1
        pos[rob] = but
        last_time[rob] = elapsed
    return elapsed

def do_test(input):
    line = input.readline().strip(' \r\n\t').split()
    M = int(line[0])
    buttons = []
    for i in range(M):
        ind = int(line[i*2+2])
        buttons.append((0, ind) if line[i*2+1]=='O' else (1, ind))
    res = solve(buttons)
    return str(res)

input = sys.stdin

N = int(input.readline())

for test in range(N):
    answer = do_test(input)
    print 'Case #%d: %s' % (test+1, answer)
    sys.stdout.flush()
    

