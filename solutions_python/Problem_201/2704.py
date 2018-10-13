'''
Created on Apr 8, 2017

@author: Vicki
'''

def bestSpot(spots, ppl):
    
    #construct original bathroom
    if ppl > spots:
        return "IMPOSSIBLE TO FIT'EM ALL!"
    room = [1]
    for i in range(spots):
        room.append(0)
    room.append(1)
    
    occupied = [0,spots+1] #first and last occupied
    spotsInBetween = []
    
    for j in range(ppl):
        spotsInBetween = []
        for k in range(len(occupied)-1):
            spotsInBetween.append(occupied[k+1]-occupied[k]-1) #a list of num of spots in between two occupied ones
        maxSpotsInBetween = max(spotsInBetween)
        helperInd = [ind for ind in range(len(spotsInBetween)) if spotsInBetween[ind]==maxSpotsInBetween][0]
        
        spotInd = (occupied[helperInd+1] + occupied[helperInd])/2
        occupied.append(spotInd)
        occupied = sorted(occupied)
    pos = occupied.index(spotInd)
    toLeft = spotInd - occupied[pos-1] -1
    toRight = occupied[pos+1] - spotInd - 1
    
    return (max(toLeft, toRight), min(toLeft, toRight))


def readFile(fname):
    f = open(fname)
    liste = []
    for line in f:
        liste.append(line)
    f.close()
    return liste
 
 
fileAsList = readFile("C-small-1-attempt0.txt")
t = int(fileAsList[0])
 
 
for i in range(1, t + 1):
    n, m = [int(s) for s in fileAsList[i].split(" ")]  # read a list of integers, 2 in this case
    j,k = bestSpot(n,m)
    print("Case #{}: {} {}".format(i, j, k))
