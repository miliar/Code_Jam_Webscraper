def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case

        stallRanges = {}
        stallRanges[n+1] = [[0,n+1]]
        person = 1

        while person < m:
            possibleLocations = max(stallRanges.keys())
            killLocation = min(stallRanges[possibleLocations])
            newLocation = [killLocation[0], killLocation[0]+((killLocation[1] - killLocation[0])/2)]
            newLocation2 = [killLocation[0]+((killLocation[1] - killLocation[0])/ 2), killLocation[1]]

            if stallRanges.has_key(newLocation[1]-newLocation[0]):
                newLocationItems = stallRanges[newLocation[1]-newLocation[0]]
                newLocationItems.append(newLocation)
            else:
                stallRanges[newLocation[1]-newLocation[0]] = [newLocation]

            if stallRanges.has_key(newLocation2[1]-newLocation2[0]):
                newLocationItems = stallRanges[newLocation2[1]-newLocation2[0]]
                newLocationItems.append(newLocation2)
            else:
                stallRanges[newLocation2[1]-newLocation2[0]] = [newLocation2]

            stallRanges[possibleLocations].remove(killLocation)

            if stallRanges[possibleLocations] == []:
                stallRanges.__delitem__(possibleLocations)

            person+=1

        possibleLocations = max(stallRanges.keys())
        killLocation = min(stallRanges[possibleLocations])
        kLoc0 = killLocation[0]
        kLoc1 = killLocation[1]
        newLocation = [kLoc0, kLoc0+((kLoc1 - kLoc0)/ 2)]
        newLocation2 = [kLoc0+((kLoc1 - kLoc0) / 2), kLoc1]
        maxVal = max(newLocation[1]-newLocation[0]-1,newLocation2[1]-newLocation2[0]-1)
        minVal = min(newLocation[1]-newLocation[0]-1,newLocation2[1]-newLocation2[0]-1)
        print "Case #{}: {} {}".format(i, maxVal, minVal)


main()