for t in range(int(raw_input())):
    A, B = map(int, raw_input().split(' '))

    seen = set()
    for i in range(A, B):
        str_i = str(i)
        for _ in range(len(str_i)-1):
            str_i = str_i[-1] + str_i[:-1]
            j = int(str_i)
            if i < j and j <= B:
                seen.add((i, j))

    print "Case #%d: %d" % (t+1, len(seen))
