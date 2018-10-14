



t = int(input())

for j in range(1, t + 1):
    n = int(input())

    ns = str(n)

    max_i = 0
    max_c = None

    isTidy = True

    for i, char in enumerate(ns):
        c_i = int(char)
        if max_c == None or c_i > max_c:
            max_c = c_i
            max_i = i
        elif max_c == c_i:
            pass
        else: # max_c < c_i
            isTidy = False
            break

    answer = ns

    if not isTidy:
        # print(c_i)
        if max_c > 1:
            # print(ns[0:max_i], str(max_i - 1), ("9" * (len(ns) - max_i - 1)))
            answer = ns[0:max_i] + str(max_c - 1) + ("9" * (len(ns) - max_i - 1))
        else:
            answer = "9" * (len(ns) - 1)

    print("Case #{}: {}".format(j, answer))
    # check format
