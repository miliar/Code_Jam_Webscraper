f = open('A-small-attempt0.in')
for x in range(int(f.readline())):
    p = int(f.readline())
    grid1 = []
    for i in range(4):
        grid1.append({int(n) for n in f.readline().split()})
    q = int(f.readline())
    grid2 = []
    for i in range(4):
        grid2.append({int(n) for n in f.readline().split()})
    candidates = grid1[p - 1] & grid2[q - 1]
    if len(candidates) == 1:
        res = str(list(candidates)[0])
    elif len(candidates) == 0:
        res = 'Volunteer cheated!'
    else:
        res = 'Bad magician!'
    print 'Case #%d: %s' % (x + 1, res)
f.close()
