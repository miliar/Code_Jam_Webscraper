for case in range(1, int(input())+1):
    s_max, audience = input().split()
    s_max = int(s_max)
    audience = list(map(int, audience))

    standing = audience[0]

    invite = 0

    for s, persons in enumerate(audience[1:], start=1):
        if s <= standing:
            standing += persons
        else:
            #print('needed %s, having %s, adding %s' % (s, standing, (s-standing)))
            invite += (s - standing)
            standing = s + persons


    print('Case #%d: %d' % (case, invite))
