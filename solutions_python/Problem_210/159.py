#!/usr/bin/python3

T = int(input())

for case in range(1, T+1):
    AC, AJ = map(int, input().split())
    Cameron = [tuple(map(int, input().split())) for i in range(AC)]
    Jamie = [tuple(map(int, input().split())) for i in range(AJ)]

    if (AC + AJ) == 1: 
        print("Case #{0}: {1}".format(case, 2))
        continue

    Activities = [tup + ('C',) for tup in Cameron] + [tup + ('J',) for tup in Jamie]
    Activities.sort(key=lambda tup: tup[0])

    prev = Activities[-1][2]
    prevEnd = Activities[-1][1] - 1440
    
    swaps = 0

    CameronTime = 0
    JamieTime = 0

    CCGaps = []
    CJGaps = 0
    JCGaps = 0
    JJGaps = []

    for act in Activities:

        if act[2] == 'C': CameronTime += act[1] - act[0]
        else: JamieTime += act[1] - act[0]

        if prev == 'C' and act[2] == 'C': CCGaps += [act[0] - prevEnd]
        if prev == 'C' and act[2] == 'J': CJGaps += act[0] - prevEnd
        if prev == 'J' and act[2] == 'C': JCGaps += act[0] - prevEnd
        if prev == 'J' and act[2] == 'J': JJGaps += [act[0] - prevEnd]
        
        if act[2] != prev: 
            swaps += 1
        
        prev = act[2]
        prevEnd = act[1]

    if CameronTime < 720:
        time = min(720 - CameronTime, CJGaps)
        CameronTime += time;
        CJGaps -= time
    JamieTime += CJGaps

    if CameronTime < 720:
        time = min(720 - CameronTime, JCGaps)
        CameronTime += time;
        JCGaps -= time
    JamieTime += JCGaps

    CCGaps = [i for i in CCGaps if i != 0]
    CCGaps.sort()

    index = 0;
    while CameronTime < 720 and index < len(CCGaps):
        time = min(720 - CameronTime, CCGaps[index])
        CameronTime += time
        CCGaps[index] -= time
        index += 1
    
    CCGaps = [i for i in CCGaps if i != 0]
    
    JamieTime += sum(CCGaps)
    swaps += 2 * len(CCGaps)

    JJGaps = [i for i in JJGaps if i != 0]
    JJGaps.sort(reverse=True)

    index = 0;
    while CameronTime < 720 and index < len(JJGaps):
        time = min(720 - CameronTime, JJGaps[index])
        CameronTime += time
        JJGaps[index] -= time
        index += 1
        swaps += 2
    
    JamieTime += sum(JJGaps)

    if (CameronTime != 720) or (JamieTime != 720): raise Exception

    print("Case #{0}: {1}".format(case, swaps))
