T = int(input())
for t in range(1, T + 1):
    r = int(input())
    for i in range(1, 5):
        a = list(map(int, input().split()))
        if i == r:
            b = a
    r = int(input())
    for j in range(1, 5):
        a = list(map(int, input().split()))
        if j == r:
            c = a
    a = [v for v in b if v in c]
    if len(a) == 0:
        print("Case #" + str(t) + ": " + "Volunteer cheated!")
    elif len(a) > 1:
        print("Case #" + str(t) + ": " + "Bad magician!")
    else:
        print("Case #" + str(t) + ": " + str(a[0]))