import sys
stdin = sys.stdin

T = int(stdin.readline())
for icase in range(T):
    x, r, c = map(int, stdin.readline().split())

    ok = True
    if r*c % x != 0:
        ok = False
    if r < x and c < x:
        ok = False
    if x > 2 and min(r, c) == 1:
        ok = False
    if x == 4 and min(r, c) == 2:
        ok = False

    print "Case #%d: %s" % (icase+1, ["RICHARD", "GABRIEL"][int(ok)])
    
