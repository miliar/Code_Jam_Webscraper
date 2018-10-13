def rpi(wp, owp, oowp):
    return 0.25 * wp + 0.50 * owp + 0.25 * oowp

n_tests = int(input())
for t in range(0, n_tests):
    nteams = int(input())
    
    teams = []
    for i in range(0, nteams):
        str_teams = input()
        
        total = 0
        win = 0
        opponments = []
        for j in range(0, nteams):
            if str_teams[j] == '1':
                opponments.append((j, True))
                total += 1
                win += 1
            elif str_teams[j] == '0':
                opponments.append((j, False))
                total += 1
                
        teams.append((win / total, opponments))

    # owp
    teams2 = []
    for i in teams:
        sum_oppo = 0
        for o, win in i[1]:
            if win:
                sum_oppo += teams[o][0] * len(teams[o][1]) / (len(teams[o][1]) - 1)
            else:
                sum_oppo += (teams[o][0] * len(teams[o][1]) - 1) / (len(teams[o][1]) - 1)

        teams2.append((i[0], i[1], sum_oppo / len(i[1])))

    #print (teams2)
    #oowp
    teams3 = []
    for i in teams2:
        sum_oppo = 0
        for o, win in i[1]:
            sum_oppo += teams2[o][2]

        #print (i, sum_oppo / len(i[1]))
        teams3.append(rpi(i[0], i[2], sum_oppo / len(i[1])))
        
    print ("Case #"+str(t+1)+":")
    for i in teams3:
        print (i)