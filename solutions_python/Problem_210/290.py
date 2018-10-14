t = int(input())
for i in range(1, t + 1):
    ac, aj = [int(s) for s in input().split(" ")]

    cameron = []
    jamie = []
    switch = []
    jamie_free = []
    cameron_free = []

    for k in range(ac):
        jamie.append([int(s) for s in input().split(" ")])

    for k in range(aj):
        cameron.append([int(s) for s in input().split(" ")])

    temp = cameron + jamie
    temp.sort()

    for k, slot in enumerate(temp):
        next_slot = temp[(k + 1) % len(temp)]
        if slot in cameron:
            if next_slot in cameron:
                cameron_free.append([slot[1], next_slot[0]])
            else:
                switch.append([slot[1], next_slot[0]])
        else:
            if next_slot in jamie:
                jamie_free.append([slot[1], next_slot[0]])
            else:
                switch.append([slot[1], next_slot[0]])

    if len(switch) > 0 and switch[-1][0] > switch[-1][1]:
        switch[-1][1] += 1440
    if len(cameron_free) > 0 and cameron_free[-1][0] > cameron_free[-1][1]:
        cameron_free[-1][1] += 1440
    if len(jamie_free) > 0 and jamie_free[-1][0] > jamie_free[-1][1]:
        jamie_free[-1][1] += 1440

    cameron_mins = 720
    for slot in cameron:
        cameron_mins -= slot[1] - slot[0]
    jamie_mins = 720
    for slot in jamie:
        jamie_mins -= slot[1] - slot[0]

    additional_switches = 0
    cameron_mins = cameron_mins - sum([slot[1] - slot[0] for slot in cameron_free])
    jamie_mins = jamie_mins - sum([slot[1] - slot[0] for slot in jamie_free])
    if cameron_mins < 0:
        cameron_free.sort(key=lambda x: x[1] - x[0], reverse=True)

        for slot in cameron_free:
            additional_switches += 2
            cameron_mins += (slot[1] - slot[0])
            if cameron_mins >= 0:
                break

    elif jamie_mins < 0:
        jamie_free.sort(key=lambda x: x[1] - x[0], reverse=True)

        for slot in jamie_free:
            additional_switches += 2
            jamie_mins += (slot[1] - slot[0])
            if jamie_mins >= 0:
                break

    switches = additional_switches + len(switch)
    print("Case #{}: {}".format(i, switches))