f = open("D:/Eigene Dokumente/sonstiges/CodeJam/small.txt", 'r')
nr = int(f.readline())
for case in range(nr):
    first = int(f.readline())
    poss = []
    for row in range(first-1):
        f.readline()
    poss += f.readline().split()
    for row in range(4-first):
        f.readline()
    second = int(f.readline())
    poss2 = []
    for row in range(second-1):
        f.readline()
    poss2 += f.readline().split()
    for row in range(4-second):
        f.readline()
    final = []
    for i in poss2:
        if i in poss:
            final.append(i)
    if len(final) == 0:
        print 'Case #' + str(case+1)+ ': Volunteer cheated!'
    elif len(final) == 1:
        print 'Case #' + str(case+1)+ ': ' + str(final[0])
    else:
        print 'Case #' + str(case+1)+ ': Bad magician!'
