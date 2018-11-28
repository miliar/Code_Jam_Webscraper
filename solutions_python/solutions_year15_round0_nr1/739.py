f = open('A-large.in')

lines = [line.strip() for line in f.readlines()[1:]]

for idx, line in enumerate(lines):
    num, stand = line.split()
    stand = map(int, list(stand))
    curStand = 0
    needStand = 0
    for i, p in enumerate(stand):
        if i == 0:
            curStand = stand[0]
            continue
        if curStand < i and p > 0:
            needStand += i - curStand 
            curStand += p + (i-curStand)
        else:
            curStand += p
    print 'Case #%d: %d' % (idx + 1, needStand) 
