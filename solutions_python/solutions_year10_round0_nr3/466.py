for case in xrange(int(raw_input())):
    R, k, N = map(int, raw_input().split())
    g = map(int, raw_input().split())

    i = 0
    money = 0
    while R:
        people = 0
        sindex = i
        while True:
            peopleplus = people + g[i]
            if peopleplus > k:
                break
            people = peopleplus
            i += 1
            if i >= N:
                i%=N
            if i == sindex:
                break
        money += people
        R -= 1
    
    print "Case #%d:"%(case+1),money
