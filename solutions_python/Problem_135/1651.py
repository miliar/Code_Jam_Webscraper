def inters(l1, l2):
    r = []
    for i in l1:
        if i in l2:
            r.append(i)
    return r

t = int(input())
for tc in range(1, t+1):
    firstrow = int(input())
    for i in range(1, 5):
        inp = input()
        if i == firstrow:
            firstarranglist = [int(x) for x in inp.split()]
    secondrow = int(input())
    for i in range(1, 5):
        inp = input()
        if i == secondrow:
            secondarranglist = [int(x) for x in inp.split()]
    y = inters(firstarranglist, secondarranglist)
    if len(y) == 0:
        print('Case #%i: Volunteer cheated!' % (tc))
    elif len(y) == 1:
        print('Case #%i: %i' % (tc, y[0]))
    else:
        print('Case #%i: Bad magician!' % (tc))
