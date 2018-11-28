
def magicka(filename):
    f = open(filename, "r")
    
    T = int(f.readline())
    
    missions = []
    for case in range(T):
        line = f.readline()
        seq = line.split()
        missions.append(seq)
        
    f.close()
    
    f = open(filename+".out", "w")
    
    for i in range(len(missions)):
        mission = missions[i]
        
        print "mission", mission
        
        C = int(mission[0]) 
        combs = {}
        for j in range(1,C+1):
            comb = mission[j]
            print "comb", comb
            combs[frozenset([comb[0],comb[1]])] = comb[2]
            
        D = int(mission[C+1])
        opps = {}
        for j in range(C+2,C+2+D):
            opp = mission[j]
            print "opp", opp
            opps[opp[0]] = opp[1]
            opps[opp[1]] = opp[0]
        
        # N = int(mission[C+2+D])
        # seq = mission[C+2+D:C+2+D+N-1]
        seq = mission.pop()
        print "seq", seq
        
        result = []
        for symb in seq:
            print result
            if result == []:
                result.append(symb)
            else:
                last = result.pop()
                comb = frozenset([last,symb])
                if combs.has_key(comb):
                    result.append(combs[comb])
                else:
                    result.append(last)
                    result.append(symb)
                    
                    if opps.has_key(symb):
                        opp = opps[symb]
                        if opp in result:
                            result = []
        
        if len(result) == 0:
            seqstring = ""
        else:
            seqstring = result[0]
            for j in range(1, len(result)):
                seqstring = seqstring + ", " + result[j]
            
        print "Case #"+str(i+1)+": ["+seqstring+"]"
        print 50*"-"
        f.write("Case #"+str(i+1)+": ["+seqstring+"]" + "\n")
        
    f.close()
                
                
            
            
            
            