tn = int(input())
for test in range(tn):
    r1 = int(input()) - 1
    a = [[int(x) for x in input().split()] for i in range(4)]
    r2 = int(input()) - 1
    b = [[int(x) for x in input().split()] for i in range(4)]
    v = [x for x in a[r1] if x in b[r2]]
    if len(v) == 0:
        print("Case #%d: Volunteer cheated!" % (test + 1))
    elif len(v) > 1:
        print("Case #%d: Bad magician!" % (test + 1))
    else:
        print("Case #%d: %d" % (test + 1, v[0]))
