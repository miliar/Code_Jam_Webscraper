
def rpi(filename):
    f = open(filename, "r")
    T = int(f.readline())
    
    fo = open(filename+".out", "w")

    for t in range(0,T):
        beat = {}
        played = {}
        N = int(f.readline())
        for i in range(0,N):
            beat[i]=set()
            played[i]=set()
            line = f.readline()
            for j,char in enumerate(line):
                if char=="1":
                    beat[i].add(j)
                if char in ["0","1"]:                 
                    played[i].add(j)

        wp = dict( (team, float(len(beat[team]))/len(played[team])) for team in played )
        wpwo = {}
        for team in range(0,N):
            without = {}
            for other in played[team]:
                wpwo[(other, team)] = float(len(beat[other].difference([team])))/len(played[other].difference([team]))

        owp = {}
        for team in range(0,N):
            owp[team] = reduce(lambda x,y: x+wpwo[(y,team)], played[team], 0.) / len(played[team])

        fo.write("Case #"+str(t+1)+":\n")
        score = {}
        for team in range(0,N):
            oowp = reduce(lambda x,y: x+owp[y], played[team], 0.) / len(played[team])
            score[team] = 0.25*wp[team] + 0.5*owp[team] + 0.25*oowp
            fo.write(str(score[team])+"\n")

    
    fo.close()
    f.close()

                
                
            
            
            
            