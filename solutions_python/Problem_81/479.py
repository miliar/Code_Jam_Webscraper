def get_score(list):
    dot = 0
    won = 0
    lost= 0
    for l in list:
        if l == '.':
            dot += 1
        elif l == '1':
            won += 1
        else:
            lost += 1
    return (dot, won, lost)

def main():
    filename = 'A-large'
    
    inf = open(filename + '.in', 'r')
    outf = open(filename + '.out', 'w')
    
    T = int(inf.readline().strip().split()[0])
    print "Number of Cases: %d" % T
    
    for num_case in range(1, T + 1):
        buf = 'Case #%d:\n' % num_case
#        print 'Case #%d' % num_case
        num_data = int(inf.readline().strip().split()[0])
#        num_data = 1
        print 'Team: %d' % num_data
#        N, Pd, Pg = (0, 0, 0)
        data = []
        for i in range(num_data):
            data.append(list(inf.readline().strip()))
        print data
        
        WP = [0 for i in range(num_data)]
        OWP = [0 for i in range(num_data)]
        OOWP = [0 for i in range(num_data)]
        RPI = [0 for i in range(num_data)]
        
        score = []
        for d in data:
            score.append(get_score(d))
        
        for team in range(num_data):
            dot, won, lost = score[team]
            WP[team] = float(won) / (won + lost)
        print 'WP', WP
        for team in range(num_data):
            dot, won, lost = score[team]
            for opp in range(num_data):
                if data[team][opp] == '1':
                    OWP[team] += float(score[opp][1]) / (score[opp][1] + score[opp][2] - 1)
                elif data[team][opp] == '0':
                    OWP[team] += float(score[opp][1] - 1) / (score[opp][1] + score[opp][2] - 1)
            OWP[team] /= float(score[team][1] + score[team][2])
        print 'OWP', OWP
        for team in range(num_data):
            dot, won, lost = score[team]
            for opp in range(num_data):
                if data[team][opp] != '.':
                    OOWP[team] += OWP[opp]
            OOWP[team] /= float(num_data - dot)
#            print 'OOWP', OOWP
            
#            RPI[team] = 0.25 * WP[team] + 0.5 * OWP[team] + 0.25 * OOWP[team]
            buf += '%.11f\n' % (0.25 * WP[team] + 0.5 * OWP[team] + 0.25 * OOWP[team])
        
        print buf
        outf.write(buf)
    inf.close()
    outf.close()

if __name__ == '__main__':
    main()
    
