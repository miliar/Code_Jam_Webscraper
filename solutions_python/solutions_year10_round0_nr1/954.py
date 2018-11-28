class Snapper:
    def __init__(self, prev, curr):
        self.prev = prev
        self.curr = curr

total = raw_input()
total = int(total)
cases = {}
for case in range(0,total):
    line = raw_input()
    cases[case] = line

kcases = cases.keys()
kcases.sort()
for case in kcases:
    (nlen, klen) = cases[case].split(" ")
    nlen = int(nlen)
    klen = int(klen)

    snappers = []
    for i in range(0,nlen):
        if i == 0:
            snappers.append(Snapper(1, 0))
        else:
            snappers.append(Snapper(0, 0))

    for snap in range(0,klen):
        for i in range(0, len(snappers)):
            if (snappers[i].prev == 1):
                if snappers[i].curr == 0:
                    snappers[i].curr = 1
                else:
                    snappers[i].curr = 0
        for i in range(0, len(snappers)):
            if i < len(snappers) - 1:
                if snappers[i].prev == 1 and snappers[i].curr == 1:
                    snappers[i+1].prev = 1
                else:
                    snappers[i+1].prev = 0

    if snappers[-1].curr == 1 and snappers[-1].prev == 1:
        bulb = "ON"
    else:
        bulb = "OFF"

    print "Case #%d: %s" % (case+1, bulb)
