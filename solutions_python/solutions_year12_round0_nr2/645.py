

class DancerTrip(object):
    def __init__(self, totalPoints):
        self.totalPoints = totalPoints
        self.usualBest = (totalPoints + 2) / 3  # int division, add 2 so we can ignore the remainder
        self.usualBest = min(self.usualBest, 10) # problem definition says max will be 10
        self.surprisingValue = (totalPoints + 4) / 3
        self.surprisingValue = min(self.surprisingValue, 10) # problem definition says max will be 10
        # careful for boundary conditions (we don't care too much about 
        if (self.totalPoints == 0):
            self.surprisingValue = 0

    def __repr__(self):
        return "TP=" + str(self.totalPoints) + "; best=" + str(self.usualBest)  + "; surprise=" + str(self.surprisingValue)

    def isBestResultAtLeast(self, min_p):
        if (self.usualBest >= min_p):
            return True
        return False

    def isSurpisinglyAtLeast(self, min_p):
        if (self.surprisingValue >= min_p):
            return True
        return False


class DancingGooglersEvent(object):
    def __init__(self, inputs):  # inputs will contain the whole line. N S p ti0 ti1... tiN
        inData = inputs.split()
        self.numScores = inData[0]
        self.numSurpriseScores = int(inData[1])
        self.bestMinP = int(inData[2])
        del inData[:3] # remove from start to the 3rd element
        self.dancerTriplets = [DancerTrip(int(score)) for score in inData]

    def getAnswer(self):
        dancersWithMinBest = [dancer for dancer in self.dancerTriplets
                              if (dancer.isBestResultAtLeast(self.bestMinP))]
        nonAchievingDancers = [dancer for dancer in self.dancerTriplets
                              if (dancer.isBestResultAtLeast(self.bestMinP) == False)]
        dancersWithSurpriseScore = [dancer for dancer in nonAchievingDancers
                              if (dancer.isSurpisinglyAtLeast(self.bestMinP))]
        return len(dancersWithMinBest) + min(self.numSurpriseScores, len(dancersWithSurpriseScore))
        
    def __repr__(self):
        msg = "N=" + str(len(self.dancerTriplets)) 
        msg += ", Surprises=" + str(self.numSurpriseScores) 
        msg += ", bestResultMinP=" + str(self.bestMinP)
        #msg += ", triplets=" + str(self.dancerTriplets)
        msg += ", answer=" + str(self.getAnswer())
        return msg


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        filename = "input.in"
    else:
        filename = sys.argv[1]

    read_file = file(filename)
    file_contents = list(read_file.readlines())
    del file_contents[0] # skip first line of input since it's just the number of test cases
    counter = 1
    for line in file_contents:
        print "Case #" + str(counter) + ": " + str(DancingGooglersEvent(line).getAnswer())
        counter += 1

