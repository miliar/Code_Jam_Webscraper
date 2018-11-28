T = int(input())
test = 1

while test <= T:
    print("Case #" + str(test) + ": ", end="")
    test += 1

    num = int(input())

    aaa = [float(a) for a in input().split()]
    bbb = [float(a) for a in input().split()]

    aaa.sort()
    bbb.sort()

    # find A

    a = num-1
    b = num-1
    a_count = 0

    while b >= 0:
        if aaa[a] > bbb[b]:
            a_count += 1
            a -= 1
            b -= 1
        else:
            b -= 1

    # find B

    a = num - 1
    b = num - 1
    b_count = 0

    while a >= 0:
        if aaa[a] < bbb[b]:
            b_count += 1
            a -= 1
            b -= 1
        else:
            a -= 1

    print(a_count, num - b_count)