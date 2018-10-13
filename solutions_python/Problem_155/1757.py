for t in range(input()):
    print "Case #%s:" % str(t + 1),
    standing = 0
    to_add = 0
    for (i, c) in enumerate(map(int,raw_input().split()[1])):
        # print i ,c
        if i > standing:
            to_add += i - standing
            standing += i - standing
        standing += c
    print to_add