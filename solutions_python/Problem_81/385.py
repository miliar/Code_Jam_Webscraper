import sys
with open(sys.argv[1]) as f:
    T = int(f.next())
    for case in range(T):
        n = int(f.next())
        d = dict([(x,[]) for x in range(n)])
        for y in range(n):
            data = f.next().strip()
            for i in data:
                d[y].append(i)
        #calculate WP and specific OWP
        WP = {}
        #stats for team #(team)
        for team in d:
            wins = 0
            games = 0
            #WP without team x
            oWins = dict([[x,0] for x in range(n)])
            oGames = dict([[x,0] for x in range(n)])
            #iterate through each opponent, opponent is o_team
            for o_team in range(n):
                win = d[team][o_team]
                if win=='1':
                    wins += 1
                    for t in oWins:
                        if t!=o_team:
                            oWins[t] += 1
                if win!='.':
                    games += 1
                    for t in oGames:
                        if t!=o_team:
                            oGames[t] += 1
            WP[team] = [float(wins)/games,{}]
            for n_o in range(n):
                if n_o!=team:
                    WP[team][1][n_o] = float(oWins[n_o])/oGames[n_o]
        #RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
        #calculate OWP
        OWP = {}
        for team in range(n):
            t_OWP_total = 0
            t_OWP_count = 0
            for o_team in range(n):
                if o_team!=team and d[team][o_team]!='.':
                    t_OWP_total += WP[o_team][1][team]
                    t_OWP_count += 1
            OWP[team] = float(t_OWP_total)/t_OWP_count
        #calculate RPI!
        print "Case #"+str(case+1)+":"
        for team in range(n):
            t_WP = WP[team][0]
            t_OWP = OWP[team]
            t_OOWP_total = 0
            t_OOWP_count = 0
            for o_team in range(n):
                if o_team!=team and d[team][o_team]!='.':
                    t_OOWP_total += OWP[o_team]
                    t_OOWP_count += 1
            t_OOWP = float(t_OOWP_total)/t_OOWP_count
            RPI = 0.25*t_WP + 0.50*t_OWP + 0.25*t_OOWP
            print RPI