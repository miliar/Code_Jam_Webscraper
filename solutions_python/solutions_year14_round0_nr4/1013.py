# Code Jam 2014 - Qualification Round
# Problem D: Deceitful War
# chamrtom


T = int(raw_input())

for t in range(1, T+1):
    N = int(raw_input())
    naomi = map(float, raw_input().split())
    naomi.sort()
    ken = map(float, raw_input().split())
    ken.sort()

    wscore = 0
    dwscore = 0

    # Simulate game - Deceitful War
    dwnaomi = list(naomi)
    dwken = list(ken)
    for i in range(N):
        if dwnaomi[0] > dwken[0]:
            dwscore += 1
            dwnaomi.pop(0)
            dwken.pop(0)
        else:
            dwnaomi.pop(0)
            dwken.pop(-1)

    # Simulate game - War
    wnaomi = list(naomi)
    wken = list(ken)
    while len(wnaomi) > 0:
        if len(wnaomi) == 1:
            if (wnaomi[0] > wken[0]):
                wscore += 1
            wnaomi.pop(0)
            wken.pop(0)
        else:
            # naomi
            wsel = None
            for block in wnaomi:
                if block > wken[-1]:
                    wsel = block
                    wnaomi.remove(block)
                    break
            if wsel == None:
                wsel = wnaomi[0]
                wnaomi.pop(0)
            # ken
            if wsel > wken[-1]:
                wscore += 1
                wken.pop(0)
            else:
                for block in wken:
                    if block > wsel:
                        wken.remove(block)
                        break

    print "Case #{0}: {1} {2}".format(t, dwscore, wscore)
