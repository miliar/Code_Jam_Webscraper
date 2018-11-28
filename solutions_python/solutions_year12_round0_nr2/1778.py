# b_dancingwiththegooglers.py
import copy

class Scoreset:
    def __init__(self, data):
        self.number = int(data[0])
        self.surprises = int(data[1])
        self.cutoff = int(data[2])
        self.scores = list()
        self.passcount = 0
        for score in data[3:]:
            self.scores.append(IndScore(int(score), False))

class IndScore:
    def __init__(self, score, passed):
        self.passed = passed
        self.score = int(score)
        self.trip = []

    def findSimplestTriplet(self):
        score = copy.copy(self.score)
        #print "=================="
        #print "score!", score
        while (3 - len(self.trip)) > 0:
            average = score / (3 - len(self.trip))
            modulus = score % (3 - len(self.trip))
            #print average, modulus
            if modulus == 0:
                self.trip.append(int(average))
                score = score - int(average)
            elif modulus > 0:
                self.trip.append(int(average + 1))
                score = score - int(average + 1)
        #print "triplet!", self.trip

    def findSurpriseTriplet(self, cutoff):
        #there are three types of triplet spread.
        # [big, big, small]
        if self.trip[0] == self.trip[1] and self.trip[1] != self.trip[2]:
            # matrix addition: [1, -1, 0]
            self.trip[0] += 1
            self.trip[1] -= 1
            
        # [big, small, small]
        elif self.trip[0] != self.trip[1] and self.trip[1] == self.trip[2]:
            #you're fucked!
            pass
        
        # [small, small, small]
        elif self.trip[0] == self.trip[1] == self.trip[2] and self.trip[2] != 0:
            """ if self.trip[2] == 0, you're fucked!"""
            self.trip[0] += 1
            self.trip[2] -= 1
        
        return False

def getData(filename):
    f = open(filename, 'r')
    throwaway = f.readline()
    data = []
    for line in f:
        data.append(Scoreset(line.split()))
    return data

def analyzeSet(scoreset):
    for indScore in scoreset.scores:
        indScore.findSimplestTriplet()
        if indScore.trip[0] >= scoreset.cutoff:
            indScore.passed = True
            scoreset.passcount += 1
        elif scoreset.surprises > 0:
            indScore.findSurpriseTriplet(scoreset.cutoff)
            if indScore.trip[0] >= scoreset.cutoff:
                scoreset.surprises -= 1
                indScore.passed = True
                scoreset.passcount += 1
                
    #print scoreset.passcount
    return scoreset.passcount

if __name__ == "__main__":
    #data = getData("b_sample.txt")
    #data = getData("B-small-attempt0.in")
    data = getData("B-large.in")
    print len(data), data
    output = []
    print "==== the real shit"
    fout = open("fout_large.txt", 'w')
    for i in range(len(data)):
        output.append(analyzeSet(data[i]))

    for i in range(len(output)):
        fout.write("Case #" + str(i + 1) + ": " + str(output[i]) + "\n")
        
    fout.close()





