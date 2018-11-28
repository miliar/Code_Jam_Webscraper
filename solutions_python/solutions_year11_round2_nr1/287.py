import copy

def function(fi,fo):
    f = open(fi)
    f2 = open(fo,"w")
    cases = int(f.readline())
    
    for nc,case in enumerate(range(cases)):
        ne = int(f.readline()[0:-1])
        # ----------------------------------
        # Code here
        # ---------------------------------
        table = {}
        playedGames = {}
        wonedGames = {}
        opossitors = {}
        games = {}
        WP = {}
        OWP = {}
        OOWP = {}
        for i in range(ne):
            resultsi = f.readline()[0:-1]
            playedGames[i] = 0
            wonedGames[i] = 0
            opossitors[i] = []
            for oponent,result in enumerate(resultsi):
                games[i,oponent] = 0
                if result != ".":
                    result = int(result)
                    table[i,oponent] = result
                    games[i,oponent] = 1
                    playedGames[i] += 1
                    wonedGames[i] += result
                    opossitors[i] += [oponent]
        
        
        for team in range(ne):
            WP[team] = wonedGames[team]/float(playedGames[team])
            OWP[team] = 0 
            for opositor in opossitors[team]:
                resulto = table[opositor,team]
                OWPo = (wonedGames[opositor] - resulto)/float((playedGames[opositor]-games[team,opositor]))
                OWP[team] += OWPo
            OWP[team] = OWP[team]/float(len(opossitors[team]))

        for team in range(ne):
            OOWP[team] = 0
            for opositor in opossitors[team]:
                OOWP[team] += OWP[opositor]
            OOWP[team] = OOWP[team]/float(len(opossitors[team]))

        text = "Case #" + str(nc+1) + ":\n"
        for team in range(ne):
            text += str(0.25*WP[team] + 0.50*OWP[team] + 0.25*OOWP[team])  + "\n"   
        f2.write(text)
        

#function("test.in","test.txt")
#function("short.in","short.txt")
function("long.in","long.txt")

