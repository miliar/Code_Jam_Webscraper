
def get_vth_Raw(v):
    for i in range(4):
        if i + 1 == v:
            r = map(int, raw_input().split())
        else:
            raw_input()
    return r


t = int(raw_input())
for i in xrange(t):
    v1 = int(raw_input())
    r1 = get_vth_Raw(v1)
    v2 = int(raw_input())
    r2 = get_vth_Raw(v2)
    p = [x in r2 for x in r1]
    cs = 'Case #' + str(i + 1) + ':'
    if sum(p) == 0:
        print cs, 'Volunteer cheated!'
    elif sum(p) > 1:
        print cs, 'Bad magician!'
    else:
        print cs, r1[p.index(True)]

