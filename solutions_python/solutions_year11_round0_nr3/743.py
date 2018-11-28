""" Exhaustive enumeration from the best case """

class Candies(object):
    def __init__(self):
        pass
    
    def load(self, line):
        split = line.split(" ")
        self.candies = sorted([int(value) for value in split])

    @staticmethod
    def totalPatrickValue(values):
        total = 0
        for value in values:
            total ^= value
        return total
        
    @staticmethod
    def totalSeanValue(values):
        total = 0
        for value in values:
            total += value
        return total
        
    def split(self, splitKey):
        patricksIndices = set()
        
        index = 0
        while splitKey > 0:
            lsb = splitKey % 2
            assert 0 <= lsb < 2
            if lsb == 1:
                patricksIndices.add(index)
            index += 1
            splitKey //= 2
            
        patricks = []
        seans = []
        for (i, value) in enumerate(self.candies):
            if i in patricksIndices:
                patricks.append(value)
            else:
                seans.append(value)
        
        return (seans, patricks)
    
    def solve(self):
        numCombinations = pow(2, len(self.candies))
        for splitKey in range(1, numCombinations - 1):
            (seans, patricks) = self.split(splitKey)
            
#            v1 = self.totalPatrickValue(seans)
#            v2 = self.totalPatrickValue(patricks)
#            print "v1 = %d; v2 = %d" % (v1, v2)
            
            if self.totalPatrickValue(seans) == self.totalPatrickValue(patricks):
#                print seans
                return self.totalSeanValue(seans)
        return None
    
if __name__ == "__main__":
#    c = Candies()
#    c.load("3 5 6")
#    c.solve()

    file = open("e:\\temp\\C-small-attempt0.in")
    numProblems = int(file.readline().strip())
    for i in range(numProblems):
        numCandies = int(file.readline().strip())
        c = Candies()
        c.load(file.readline().strip())
        solution = c.solve()
        
        print("Case #%d: %s" % (i + 1, str(solution) if solution is not None else "NO"))
        
    file.close()

