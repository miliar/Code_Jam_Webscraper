import math
T = int(input())
for x in range(1, T + 1):
    Ac, Aj = map(int, input().split())
    CDs = []
    for i in range(Ac):
        C, D = map(int, input().split())
        CDs.append((C, D))
    JKs = []
    for i in range(Aj):
        J, K = map(int, input().split())
        JKs.append((J, K))
    CDs = list(sorted(CDs))
    JKs = list(sorted(JKs))
    ans = 0
    if Ac == 0:
        if JKs[-1][-1] - JKs[0][0] <= 720 or 1440 + JKs[0][-1] - JKs[-1][0] <= 720:
            ans = 2
        else:
            ans = 4
    elif Aj == 0:
        if CDs[-1][-1] - CDs[0][0] <= 720 or 1440 + CDs[0][-1] - CDs[-1][0] <= 720:
            ans = 2
        else:
            ans = 4
    elif Ac == Aj == 1:
        ans = 2
    print("Case #%d: %d" % (x, ans))
