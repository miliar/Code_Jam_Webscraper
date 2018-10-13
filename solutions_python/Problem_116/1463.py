import sys
from collections import Counter
T = int(sys.stdin.readline().strip())
for t in range(T):
    m = [list(sys.stdin.readline().strip()) for i in range(4)]
    e = sum([sum([int(m[y][x]=='.') for y in range(4)]) for x in range(4)]) > 0
    w = None
    for i in range(4):
        for r in [(0,i,1,0), (i,0,0,1), (0,0,1,1), (0,3,1,-1)]:
            c = Counter()
            x,y = r[0], r[1]
            for s in range(4):
                c[m[y][x]] += 1
                x,y = x+r[2], y+r[3]
            if c['.'] == 0 and not (c['X'] and c['O']):
                w = c.most_common()[0][0]
                break
        if w: break
    sys.stdout.write("Case #%d: " % (t+1))
    if w: print("%s won" % (w))
    elif e: print("Game has not completed")
    else: print("Draw")
    sys.stdin.readline()
