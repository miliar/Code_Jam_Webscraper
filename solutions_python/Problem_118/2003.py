DEBUG = False

class Loader:
    def __init__(self,filename='data3.txt'):
        self.fp = open(filename)
        self.size = int(self.fp.readline().strip())
        self.pos = 0
        self.cache = []

    def reset(self):
        import math
        self.pos += 1
        self.fairCount = 0
        (self.minNum, self.maxNum) = map(lambda x : int(x),
                self.fp.readline().split())
        self.minSqrt = int(math.sqrt(self.minNum))
        if (self.minSqrt **2 < self.minNum):
            self.minSqrt += 1
        self.maxSqrt = int(math.sqrt(self.maxNum))+1
        if DEBUG : print "self.minNum=%d,self.maxNum=%d"%(self.minNum,self.maxNum)
        if DEBUG : print "self.minSqrtNum=%d,self.maxSqrtNum=%d"%(self.minSqrt,self.maxSqrt)
        for numSqrt in range(self.minSqrt, self.maxSqrt+1):
            num = numSqrt ** 2 # OK. I'm Square!
            if ( num > self.maxNum ) : break
            if self.isFair( numSqrt ) and self.isFair( num ) :
                if DEBUG: print 'fair!',num
                self.fairCount += 1

    def next(self):
        if DEBUG: print '====================='
        self.reset()
        return "Case #%d: %d"%(self.pos, self.fairCount)

    def isFair(self, data):
        self.cache = []
        while data>0:
            self.cache.append(data%10)
            data = data/10
        for i in range(len(self.cache)/2):
            if self.cache[0] != self.cache.pop() :
              return False
            else :
              del self.cache[0]
        return True

    def run(self):
        for i in range(self.size):
            print self.next()


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 :
      filename = sys.argv[1]
    else:
      filename = 'data3.txt'
    loader = Loader(filename)
    loader.run()
