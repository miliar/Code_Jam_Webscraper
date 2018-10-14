def playWar(naomi, ken):
    naomiPoints = 0
    while(len(naomi) != 0):
        nChosen = naomi[0]
        kChosen = ken[-1]
        for kChoice in ken:
                if kChoice > nChosen:
                    kChosen = kChoice
                    break
        if kChosen > nChosen:
           naomi.remove(nChosen)
           ken.remove(kChosen)
        else:
            naomiPoints += 1
            naomi.remove(nChosen)
            ken.remove(kChosen)
    return naomiPoints
        
def playDeceit(naomi, ken):
    naomiPoints = 0
    while(len(naomi) != 0):
        nChosen = naomi[0]
        kChosen = ken[0]
        if len(naomi) != 1:
            if nChosen < kChosen:                
                if ken[-1] < nChosen:
                    kChosen = ken[0]
                else:
                    kChosen = ken[-1]
            

        if nChosen > kChosen:
            naomiPoints += 1

        naomi.remove(nChosen)
        ken.remove(kChosen)
        continue


        nChosen = naomi[0]
        nTold = max(ken)
        if nTold > nChosen:
            naomi.remove(nChosen)
            ken.remove(ken[-1])
        else:
            naomiPoints += 1
            naomi.remove(nChosen)
            ken.remove(ken[-1])
        continue
    
        for nToldI in range(len(naomi)-1,-1,-1):
            nTold = naomi[nToldI]
            kChosen = -1
            found = False
            for kChosenI in range(len(ken)-1,-1,-1):
                if ken[kChosenI] < nTold:
                    break
                else:
                    found = True
                    kChosen = ken[kChosenI]
            if kChosen != -1:
                break

        if kChosen == -1:
            kChosen = min(ken)
        print ken
        print naomi
        print nTold, nChosen, kChosen
        raw_input()
        

        if kChosen > nChosen:
            naomi.remove(nChosen)
            ken.remove(kChosen)
        else:
            naomiPoints += 1
            naomi.remove(nChosen)
            ken.remove(kChosen)
    return naomiPoints
        
            
        
        


FILENAME = "D-large"
f = open(FILENAME + '.in', 'r')
T = int(f.readline())
output = []

for i in range(T):
    N = int(f.readline())
    naomi = map(float, f.readline().split(' ' ))
    ken = map(float, f.readline().split(' '))
    naomi.sort()
    ken.sort()


    output.append("Case #"+str(i+1)+": " + str(playDeceit(naomi[:], ken[:])) + " " + str(playWar(naomi[:], ken[:])))



f.close()
output = '\n'.join(e for e in output)
f = open(FILENAME + '.out', 'w')
f.write(output)
f.close()

