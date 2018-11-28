T = int(raw_input())
for t in range(1, T+1):
    line = raw_input().split()
    #print line[1]
    S_max = int(line[0])
    S = map(int, [line[1][i] for i in range(0, S_max + 1)])

    friends = 0
    up_people = 0
    for i in range(0, S_max + 1):
        S_i = S[i]

        if (i > up_people):
            #Add friends
            friends += i - up_people
            up_people = i
        # people whith shy level = i stand up
        up_people += S_i

    print "Case #" + str(t) + ":", friends
