import sys

def main():
    f = open(sys.argv[1], "r")
    lines = f.readlines()
    wins = {}
    games = {}
    m_ = 0
    m = 0
    case = 1
    for i in lines[1:]:
        if m_ < m:
            games[m_]={}
            wins[m_]={}
            count = 0
            for j in list(i.strip()):
                games[m_][count] = 0
                wins[m_][count] = 0
                if j=='0':
                    games[m_][count]+=1
                elif j=='1':
                    games[m_][count]+=1
                    wins[m_][count]+=1
                count+=1
            m_+=1
        else:
            if m > 0:
                calcRPI(games,wins,case)
                case+=1
            m = int(i.strip())
            m_ = 0
            games = {}
            wins = {}
    calcRPI(games,wins,case)

def calcRPI(games,wins,case):
    print "Case #%d:" % case
    WP = {}
    OWP = {}
    OOWP = {}
    tgames = {}
    twins = {}
#    print wins
#    print games

    for i in xrange(0,len(games)):
        tgames[i] = 0
        twins[i] = 0
        #print games[i]
        for j in xrange(0,len(games)):
            tgames[i] += float(games[i][j])
            twins[i] += float(wins[i][j])
        WP[i] = twins[i]/tgames[i]
    #print twins
    #print tgames
    for i in xrange(0,len(games)):
        OWP[i] = 0
        k = 0
        for j in xrange(0,len(games)):
            if j!=i and games[j][i]!=0:
                k+=1
                OWP[i]+=(twins[j]-wins[j][i])/(tgames[j]-games[j][i])
        if k > 0:
            OWP[i]/=k

    for i in xrange(0, len(games)):
        OOWP[i] = 0
        k=0
        for j in xrange(0,len(games)):
            if j!=i and games[j][i]!=0:
                OOWP[i]+=OWP[j]
                k+=1
        OOWP[i]/=k
        print 0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i] 
    #print WP, OWP, OOWP
if __name__=="__main__":
    main()
