
T = int(raw_input())
for case in range(1,T+1):
    chosen = []
    data = []
    for que in range(1,3):
        ans = int(raw_input())
        for i in range(1, 5):
            data.append(map(int, raw_input().split()))
        chosen.append(data[ans-1])
        data = []

    res = set(chosen[0]).intersection(set(chosen[1]))
    if len(res) == 1:
        print "Case #%d: %d" % (case, res.pop())
    elif len(res) >= 1 :
        print "Case #%d: Bad magician!" % case
    else:
        print "Case #%d: Volunteer cheated!" % case

