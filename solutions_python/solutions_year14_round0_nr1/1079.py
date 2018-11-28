N = int(raw_input())
for n in range(N):
    A = int(raw_input())
    for j in range(4):
        if j+1 == A:
            v = [int(x) for x in raw_input().split()]
        else:
            raw_input()

    B = int(raw_input())
    for j in range(4):
        if j+1 == B:
            w = [int(x) for x in raw_input().split()]
        else:
            raw_input()
    res = (set(v) & set(w))

    if len(res) == 0:
        print("Case #%d: Volunteer cheated!" % (n+1))
    elif len(res) == 1:
        print("Case #%d: %d" % (n+1, res.pop()))
    else:
        print("Case #%d: Bad magician!" % (n+1))

