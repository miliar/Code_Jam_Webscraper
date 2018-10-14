import operator
t = int(input())

for i in range(t):
    s = input().split(" ")
    ac = int(s[0])
    aj = int(s[1])

    activities = []
    ctot = 0
    jtot = 0

    for _ in range(ac):
        s = input().split(" ")
        start = int(s[0])
        end = int(s[1])
        activities.append((start, end, "cameron"))
        ctot+=end-start

    for _ in range(aj):
        s = input().split(" ")
        start = int(s[0])
        end = int(s[1])
        activities.append((start, end, "jamie"))
        jtot+=end-start

    activities.sort(key=operator.itemgetter(0))

    cgaps=[]
    jgaps=[]


    for j in range(len(activities)):
        current = activities[j]
        adjacent = activities[(j+1)%len(activities)]
        if current[2] == "cameron" and adjacent[2]=="cameron":
            cgaps.append((adjacent[0]-current[1])%(60*24))        
        if current[2] == "jamie" and adjacent[2]=="jamie":
            jgaps.append((adjacent[0]-current[1])%(60*24))

    cgaps.sort()
    jgaps.sort()

    cskip=0
    jskip=0

    while cgaps and ctot+cgaps[0] <= 720:
        ctot+=cgaps[0]
        cgaps.pop(0)
        cskip+=1
    while jgaps and jtot+jgaps[0] <= 720:
        jtot+=jgaps[0]
        jgaps.pop(0)
        jskip+=1


    swaps = 0
    for j in range(len(activities)):
        current = activities[j]
        adjacent = activities[(j+1)%len(activities)]
        if current[2] == "cameron" and adjacent[2]=="cameron":
            if cskip > 0:
                cskip-=1
            else:
                swaps+=2
        elif current[2] == "jamie" and adjacent[2]=="jamie":
            if jskip > 0:
                jskip-=1
            else:
                swaps+=2
        else:
            swaps+=1

    print("Case #{}: {}".format(i+1, swaps))