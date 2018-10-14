for i in range(int(input())):
    f_row = int(input())
    for j in range(4):
        if j == f_row - 1:
            S = set(map(int, input().split()))
        else:
            a = input()
    s_row = int(input())
    for j in range(4):
        if j == s_row - 1:
            M = set(map(int, input().split()))
        else:
            a = input()
    Both = S.intersection(M)
    if len(Both) == 1:
        print("Case #" + str(i + 1) + ": " + str(list(Both)[0]))
    elif len(Both) > 1:
        print("Case #" + str(i + 1) + ": " + "Bad magician!")
    else:
        print("Case #" + str(i + 1) + ": " + "Volunteer cheated!")
