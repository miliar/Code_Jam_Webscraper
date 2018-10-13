total = raw_input()
total = int(total)
cases = {}
for case in range(0,total):
    line = raw_input()
    gline = raw_input()
    cases[case] = (line, gline)

kcases = cases.keys()
kcases.sort()
for case in kcases:
    (line, gline) = cases[case]
    (max,ppl,grps) = line.split(" ")
    (max,ppl,grps) = (int(max), int(ppl), int(grps))
    groups = gline.split(" ")

    for i in range(0,len(groups)):
        groups[i] = int(groups[i])

    income = 0
    for ride in range(0,max):
        ridecost = 0
        ride = []
        while ridecost+groups[0] <= ppl:
            group = groups.pop(0)
            ridecost = ridecost + group
            ride.append(group)
            if groups == []:
                break
        income = income + ridecost
        for group in ride:
            groups.append(group)

    print "Case #%d: %d" % (case+1, income)
