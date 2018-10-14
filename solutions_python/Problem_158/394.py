T = int(input())

for test in range(1, T + 1):
    X, R, C = [int(x) for x in input().split()]
    print("Case #%d: " % test, end="")
    if X == 1:
        print("GABRIEL")
    elif X == 2:
        if (R * C) % 2 == 0:
            print("GABRIEL")
        else:
            print("RICHARD")
    elif X == 3:
        if (R * C) % 3 != 0 or R == 1 or C == 1:
            print("RICHARD")
        else:
            print("GABRIEL")
    else:
        if R * C == 12 or R * C == 16:
            print("GABRIEL")
        else:
            print("RICHARD")
