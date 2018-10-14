import sys
import math

def solve(N, S, p, sc):
    res = 0
    can_grow = 0
    can_shrink = 0
    neutral = 0
    for s in sc:
        smin = s//3
        smax = smin
        if s%3!=0:
            smax += 1
        if_ok = (smax>=p)
        if if_ok:
            res += 1
        x0 = (s-2)//3
        x1 = x0+2
        x2 = s-x0-x1
        if x1>10 or x0<0:
            continue
        if_surp = (x1>=p)
        if if_ok==if_surp:
            neutral += 1
        elif if_ok:
            can_shrink +=1
        else:
            can_grow += 1
    gr = min(S, can_grow)
    S -= gr
    res += gr
    S -= min(S, neutral)
    shr = min(S, can_shrink)
    res -= shr
    return res

def readline():
    return input.readline().strip(' \r\n\t')

def do_test(input):
    line = readline().split()
    N = int(line[0])
    S = int(line[1])
    p = int(line[2])
    sc = [int(s) for s in line[3:]]
    res = solve(N, S, p, sc)
    return str(res)

input = sys.stdin

N = int(readline())

for test in range(N):
    answer = do_test(input)
    print 'Case #%d: %s' % (test+1, answer)
    sys.stdout.flush()
    
