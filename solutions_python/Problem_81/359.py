import sys 

isprint = False 
#isprint = True 
def comment(t):
    if(isprint): print t
def cal_wp(s,team):
    return float(s.count('1'))/float(team -s.count('.')) 
if __name__ == '__main__':
    data = open(sys.argv[1])
    n_case = int(data.readline().strip())
    for n in xrange(1,n_case+1):
        team = int(data.readline().strip())
        schedule = []
        result = []
        all_wp = []
        all_owp = []
        all_oowp = []
        for t in xrange(team):
            schedule.append(data.readline().strip()) 

        for t in xrange(team):
            all_wp.append(cal_wp(schedule[t],team))

        for t in xrange(team):
            owp = 0
            c = 0
            f = filter(lambda x: x!= t,range(team))
            for r in f:
                if schedule[t][r] != '.':
                    s = schedule[r][0:t] + schedule[r][t+1:]
                    comment('s : %s'%s)
                    owp += cal_wp(s,team-1)
                    comment('owp : %s'%owp)
                    c += 1
            owp /= c        
            all_owp.append(owp)
           
        for t in xrange(team):
            oowp = 0
            c = 0
            f = filter(lambda x: x!= t,range(team))
            for r in f:
                if schedule[t][r] != '.':
                    oowp += all_owp[r]
                    c += 1
            oowp /= c        
            all_oowp.append(oowp)

        comment(repr(all_wp))
        comment(repr(all_owp))
        comment(repr(all_oowp))
        print "Case #%d:"%n
        for i in xrange(team): 
            print all_wp[i]*0.25 + all_owp[i]*0.5 + all_oowp[i]*0.25


