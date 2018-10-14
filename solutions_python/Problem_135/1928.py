

f = open(r"e:\downloads\A-small-attempt0.in", "r")
#f = open(r"e:\downloads\magic_trick.txt", "r")

T = int(f.readline())
for t in range(1, T+1):
    row1 = int(f.readline())
    A1 = []
    for _ in range(4):
        A1.append(map(int, f.readline().split()))

    S1 = set(A1[row1-1])

    row2 = int(f.readline())
    A2 = []
    for _ in range(4):
        A2.append(map(int, f.readline().split()))

    S2 = set(A2[row2-1])

    S = S1.intersection(S2)
    if len(S) > 1:
        res = "Bad magician!"
    elif len(S) == 0:
        res = "Volunteer cheated!"
    else:
        res = str(S.pop())
    print("Case #%d: %s" % (t, res))