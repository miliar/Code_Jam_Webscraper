T = int(raw_input())

for i in range(T):
    ans1 = int(raw_input())-1
    A1 = [[int(x) for x in raw_input().split()] for _ in range(4)]
    ans2 = int(raw_input())-1
    A2 = [[int(x) for x in raw_input().split()] for _ in range(4)]
    count = 0
    force = -1
    for x in A1[ans1]:
        if x in A2[ans2]:
            count += 1
            force = x
    res = str(force)
    if count == 0:
        res = 'Volunteer cheated!'
    elif count > 1:
        res = 'Bad magician!'
    print 'Case #%d: %s' % (i+1, res)
