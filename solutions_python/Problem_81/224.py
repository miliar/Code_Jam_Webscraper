import sys

f = open(sys.argv[1], "r")
output = open(sys.argv[1] + ".results", "w+")

num_cases = int(f.readline()) # kill the first line, no. of test cases

for i in range(0, num_cases):
    output.write("Case #%d:\n" % (i+1))

    scheds = []
    all_owp = []
    all_wp = []
    num_teams = int(f.readline())
    for n in range(0, num_teams):
        sched_str = f.readline()
        sched = []

        for j in range(0, len(sched_str)):
            c = sched_str[j]
            if (c == '.'):
                pass
            elif (c == '1'):
                sched.append((j, 1))
            elif (c == '0'):
                sched.append((j, 0))
        scheds.append(sched)

    for j in range(0, len(scheds)):
        this_sched = scheds[j]

        WP = 0.0
        for (opp, result) in this_sched:
            WP += result
        WP = WP / float(len(this_sched))
        all_wp.append(WP)

        opp_wps = []
        for k in range(0, len(scheds)):
            if (k == j):
                continue
            
            played = False
            for (opp, result) in scheds[k]:
                if (opp == j):
                    played = True
                    break
            if not played:
                continue
            
            this_wp = 0.0
            num_opp = 0.0
            for (opp, result) in scheds[k]:
                if (opp == j):
                    continue
                this_wp += result
                num_opp += 1.0
            this_wp = this_wp / num_opp
            opp_wps.append(this_wp)
        OWP = float(sum(opp_wps)) / float(len(opp_wps))
        all_owp.append(OWP)
        
    for j in range(0, len(scheds)):
        opp_owps = []
        for k in range(0, len(all_owp)):
            if (k == j):
                continue
            
            played = False
            for (opp, result) in scheds[k]:
                if (opp == j):
                    played = True
                    break
            if not played:
                continue            
            
            opp_owps.append(all_owp[k])
        OOWP = float(sum(opp_owps)) / float(len(opp_owps))
        
        RPI = all_wp[j] * 0.25 + all_owp[j] * 0.50 + OOWP * 0.25
        print RPI
        output.write("%.12f\n" % (RPI))

f.close()
output.close()