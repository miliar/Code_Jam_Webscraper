fileIn = open('A-small-attempt0.in', 'r')

for case in range(1, int(fileIn.readline(), 10) + 1):
    choice = int(fileIn.readline(), 10)
    original = []
    for x in range(4):
        line = fileIn.readline()
        if x + 1 == choice:
            original = [ int(t) for t in line.split() ]

    change = []
    choice = int(fileIn.readline(), 10)
    for x in range(4):
        line = fileIn.readline()
        if x + 1 == choice:
            change = [ int(t) for t in line.split() ]

    # print original
    # print change

    match = set.intersection(*[ set(original), set(change)])
    l = len(match)
    res = ""
    if l == 1: res = next(iter(match))
    elif l > 1: res = "Bad magician!"
    else: res = "Volunteer cheated!"
    print "Case #%d: %s" % (case, res)
