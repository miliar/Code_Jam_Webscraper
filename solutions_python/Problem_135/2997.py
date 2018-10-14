def getAnswerRow(f):
    a1 = int(f.readline())
    a1Row = []
    for i in range(a1):
        a1Row = [int(x) for x in f.readline().split()]

    for i in range(4-a1):
        f.readline()

    return a1Row

f = open('C:/Users/rob/Downloads/a-small-attempt0.in', 'r')
T = int(f.readline())

for n in range(T):
    a1Row = getAnswerRow(f)
    a2Row = getAnswerRow(f)

    matches = []
    for c in a1Row:
        if c in a2Row:
            matches.append(c)

    if len(matches) == 1:
        result = matches[0]
    elif len(matches) > 1:
        result = "Bad magician!"
    else:
        result = "Volunteer cheated!"

    print('Case #{0}: {1}'.format(str(n + 1), str(result)))