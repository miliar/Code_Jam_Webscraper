T = int(raw_input())
for _t in range(T):
    a1 = int(raw_input())
    arr = []
    for r in range(4):
        arr.append(map(int, raw_input().strip().split()))
    a2 = int(raw_input())
    arr2 = []
    for r in range(4):
        arr2.append(map(int, raw_input().strip().split()))
    possibilities = set(arr[a1-1]) & set(arr2[a2-1])
    print "Case #%d:" % (_t + 1),
    if len(possibilities) == 1:
        print possibilities.pop()
    elif len(possibilities) > 1:
        print "Bad magician!"
    else:
        print "Volunteer cheated!"