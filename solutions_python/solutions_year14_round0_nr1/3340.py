T = int(raw_input())

template = "Case #{}: {}"


for i in range(1, T+1):
    a1 = int(raw_input())
    for j in range(1, 5):
        buf = set(map(int, raw_input().split()))
        if j == a1:
            row1 = buf

    a2 = int(raw_input())
    for j in range(1, 5):
        buf = set(map(int, raw_input().split()))
        if j == a2:
            row2 = buf

    res = row1.intersection(row2)

    if len(res) == 1:
        print template.format(i, res.pop())
    elif len(res) == 0:
        print template.format(i, "Volunteer cheated!")
    else:
        print template.format(i, "Bad magician!")
