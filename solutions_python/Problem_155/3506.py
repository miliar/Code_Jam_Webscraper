for case in range(int(input())):
    _, shyness = input().split()
    friends = 0 # number of required friends
    cur = 0 # number of currently standing people

    # convert a string of single digits to a list of ints
    shyness = [int(c) for c in shyness]

    for r, n in enumerate(shyness):
        if n > 0:
            friends += max(0, r - cur)
            cur += n + friends

    print("Case #{0}: {1}".format(case + 1, friends))
