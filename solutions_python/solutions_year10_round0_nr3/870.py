# Google Code Jam
# Qualifier
# C: Theme Park

class RiderQueue():
    profitPerCustomer = 1
    
    def __init__(self, R, k, N, g):
        self.R = R
        self.k = k
        self.N = N
        self.g = g
        self.currentIndex = 0

        self.totalProfit = 0
        for i in range(self.R):
            self.totalProfit += self.maxRiders() * self.profitPerCustomer

    def maxRiders(self):
        tail = self.currentIndex
        temp = 0
        for g in range(self.N):
            current = int(self.g[self.currentIndex])
            if (temp + current) > self.k:
                break

            temp += current
            self.currentIndex = (self.currentIndex+1) % self.N
            
            # break if we go through the queue completely
            if self.currentIndex==tail:
                break

        return temp
    
def testCase(RkN, g):
    inputs = RkN.split(' ')
    q = RiderQueue(int(inputs[0]), int(inputs[1]), int(inputs[2]), g.split(' '))
    return q.totalProfit

with file("C-small-attempt0.in") as f:
    T = int(f.readline())
    for i in range(T):
        result = testCase(f.readline(), f.readline())
        print "Case #" + str(i+1) + ": " + str(result)
