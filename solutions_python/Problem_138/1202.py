def toldNaomi(chosenNaomi, ken):
    
    toldNaomi = [x for x in ken if x > chosenNaomi]
    if(chosenNaomi > min(ken)):
        toldNaomi = max(ken) + 0.000001
    else:
        toldNaomi = max(ken) - 0.000001

    return toldNaomi

with open("D-large.in","r") as fp:
    with open("ouput.out","w") as out:
        cases = fp.readline()
        
        for t in range(0,int(cases)):
            
            N = fp.readline()
            
            naomi = [float(i) for i in fp.readline().split(" ")]
            ken = [float(i) for i in fp.readline().split(" ")]
            kenDeceitful = list(ken) 
                        
            pointsNaomi_DeceitfulWar = 0
            pointsNaomi_War = 0

            for n in range(0, int (N)):
                chosenNaomi = min(naomi)
                fakeChosenNaomi = toldNaomi(chosenNaomi, kenDeceitful)
                index = naomi.index(chosenNaomi)
                del naomi[index]
                
                possible = [x for x in ken if x > chosenNaomi]
                possibleDeceitful = [x for x in kenDeceitful if x > fakeChosenNaomi]
                
                if(len(possible) > 0):
                    chosenKen = min(possible)
                else:
                    chosenKen = min(ken)
                    
                index = ken.index(chosenKen)
                del ken[index]
                
                if(len(possibleDeceitful) > 0):
                    chosenKenDeceitful = min(possibleDeceitful)
                else:
                    chosenKenDeceitful = min(kenDeceitful)
                    
                index = kenDeceitful.index(chosenKenDeceitful)
                del kenDeceitful[index]
                
                if(chosenNaomi > chosenKenDeceitful):
                    pointsNaomi_DeceitfulWar = pointsNaomi_DeceitfulWar + 1;
                    
                if(chosenNaomi > chosenKen):
                    pointsNaomi_War = pointsNaomi_War + 1;
                    
            #print(pointsNaomi_DeceitfulWar, pointsNaomi_War)
            out.write("Case #" + str(t+1) + ": " + str(pointsNaomi_DeceitfulWar) + " " + str(pointsNaomi_War) + "\n")
            
            