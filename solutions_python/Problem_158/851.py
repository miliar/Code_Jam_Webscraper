for case in range(int(input())):
    # dimension, rozmery
    X, R, C = map(int, input().split())
    print("Case #{}: ".format(case + 1), end='')
    if R > X - 2 and C > X - 2 and (not (R * C) % X) and X < 7:
        print("GABRIEL")
    else:
        print("RICHARD")
