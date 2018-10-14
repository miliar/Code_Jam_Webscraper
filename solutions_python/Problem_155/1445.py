for case in range(int(raw_input())):
    data = raw_input().split()
    maxshy = int(data[0])
    shy = map(int, data[1])
    have, require = 0, 0
    for i in range(maxshy+1):
        if shy[i] and i - have > 0:
            require += i - have
            have += require + shy[i]
        else:
            have += shy[i]
    print "Case #%d: %d" % (case+1, require)
