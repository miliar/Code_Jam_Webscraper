class Loader:
    def __init__(self,filename='data2.txt'):
        self.filename = filename
        self.reset()
        self.validator = Validator()

    def reset(self):
        self.fp = open(self.filename)
        self.size = int(self.fp.readline().strip())
        self.pos = 0
        self.N = self.M = 0

    def next(self):
        self.pos += 1
        data = []
        (self.N, self.M) = map(lambda x : int(x), \
                            self.fp.readline().split())
        for i in range(self.N):
          data.append(
              map(lambda x : int(x), \
              self.fp.readline().split())
          )
        return self.validator.validate(data)

    def toStr(self, valid):
        if valid :
           result = "YES"
        else:
           result = "NO"
        return "Case #%d: %s"%(self.pos, result)

    def run(self):
        self.reset()
        for i in range(self.size):
            print self.toStr( self.next() )

class Validator:
    def __init__(self):
        self.result = []
        self.data = []

    def validate(self, data) :
        if DEBUG: print 'Validator.validate :',data
        self.resetResult(data)
        self.validateRow()
        self.validateCol()
        return self.validateResult()

    def validateResult(self):
        return self.data == self.result

    def resetResult(self,data=None):
        if data :
            self.data = data
        dimN = len(data)
        dimM = len(data[0])
        result = []
        for i in range(dimN):
            result.append([0]*dimM)
        self.result = result

    def validateRow(self):
        if DEBUG: print "validateRow:",self.data
        for index,row in enumerate(self.data):
            rowMax = row[0]
            resultRow = self.result[index]
            for i in row[1:]:
                rowMax = max(i, rowMax)
            for i in range(len(resultRow)):
                resultRow[i] = rowMax

    def validateCol(self):
        numCols = len(self.data[0])
        colMax = [0] * numCols
        for rowData in self.data:
          for colIndex, colData in enumerate(rowData):
            colMax[colIndex] = max(colMax[colIndex], colData)
        for rowData, row in enumerate(self.result):
          for colIndex, colData in enumerate(row):
              row[colIndex] = min(colData, colMax[colIndex])

DEBUG = False
def log(string):
    if DEBUG:
      print string

if __name__ == '__main__':
  loader = Loader('B-small-attempt0.in')
  loader.run()
