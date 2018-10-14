import sys

T = int(input())
for t in range(T):
    r1 = int(input())
    g1 = []
    for r in range(4):
        g1.append(input().split())

    r2 = int(input())
    g2 = []
    for r in range(4):
        g2.append(input().split())
    common = set(g1[r1-1]).intersection(set(g2[r2-1]))
    if len(common) == 1:
        print("Case #%s: %s" % (t+1, common.pop()))
    elif len(common) > 1:
        print("Case #%s: Bad magician!" % (t+1))
    else:
        print("Case #%s: Volunteer cheated!" % (t+1))
