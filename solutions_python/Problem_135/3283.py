ncases = int(input())
for case in range(ncases):
    ans1 = int(input())-1
    sor1 = []
    for n in range(4):
        sor1 += [input().split(' ')]
    ans2 = int(input())-1
    sor2 = []
    for n in range(4):
        sor2 += [input().split(' ')]

    row1 = set(sor1[ans1])
    row2 = set(sor2[ans2])
    res = row1.intersection(row2)

    if len(res) == 0:
        print ("Case #%s: Volunteer cheated!" % (case+1))
    if len(res) > 1:
        print ("Case #%s: Bad magician!" % (case+1))
    if len(res) == 1:
        print ("Case #%s: %s" % (case+1, res.pop()))



