class Loader:
    def __init__(self,filename='data1.txt') :
        self.fp = open(filename)
        self.size = int(self.fp.readline().strip())
        self.pos = 0
        self.refree = Refree()

    def next(self):
        self.pos += 1
        data = ""
        for i in range(4):
            data += self.fp.readline().strip()
        self.fp.readline()
        self.refree.judge(data)
        if DEBUG: print '< ',data
        return "Case #%d: %s"%(self.pos, Result.STR[self.refree.result])

    def run(self):
        for i in range(self.size):
            print self.next()

class Result:
    NOT_COMPLETED  = 0
    O_WON          = 1
    X_WON          = 2
    DRAW           = 3
    STR = [ "Game has not completed", "O won", "X won", "Draw" ]

class Refree :
    def __init__(self):
        self.reset()

    def reset(self):
        self.hasDot = False
        self.result = Result.NOT_COMPLETED
        self.data = None

    def toStr(self):
        return Result.STR[self.result]

    def judge(self, data):
        self.reset()
        self.data = data
        if self.checkForRow() or \
           self.checkForColumn() or \
           self.checkForDiag() : 
            return
        if self.hasDot :
            self.result = Result.NOT_COMPLETED
        else:
            self.result = Result.DRAW

    def checkForRow(self):
        ' returns true if someone won'
        log('check for row')
        for i in range(0, len(self.data), 4):
            line = self.data[i:i+4]
            if self.match( line ) :
              return True

    def checkForColumn(self):
        ' returns true if someone won'
        log('check for col')
        for col in range(0,4):
            line = []
            for row in range(0,4):
                line.append(self.data[4*row+col])
            if self.match( line ):
               return True
    
    def checkForDiag(self):
        ' returns true if someone won'
        log('check for diag')
        line1 = []
        for i in range(0, 4):
#log( 'i=',i,',data=',self.data,",5i=",(5*i)
            line1.append( self.data[5*i] )
        if self.match(line1) :
            return True
        line2 = []
        for i in range(0, 4):
            line2.append( self.data[4*i+3-i] )
        if self.match(line2) :
            return True

    def isCompleted(self):
        return self.hasDot == False

    def match(self, line):
        if "." in line:
          self.hasDot = True
          return False
        if not "O" in line:
          self.result = Result.X_WON
          log('x_won!')
          return True
        if not "X" in line:
          self.result = Result.O_WON
          log('o_won!')
          return True
        return False

DEBUG = False
def log(string):
    if DEBUG:
      print string
 
if __name__ == '__main__' :
    import sys
    if len(sys.argv) > 1 :
       filename = sys.argv[1]
    else:
       filename = 'data1.txt'
    loader = Loader(filename)
    loader.run()
