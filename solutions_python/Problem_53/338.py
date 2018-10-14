#import psyco
#psyco.full()

class memoize:
  def __init__(self, function):
    self.function = function
    self.memoized = {}

  def __call__(self, *args):
      if args not in self.memoized:
        self.memoized[args] = self.function(*args)
      return self.memoized[args]
	  
	  
from time import time
if __name__ == "__main__":
    def getInts():
        return map(int, data.readline().rstrip('\n').split(' '))
    start_time=time()
    output = open('d:/gcj/output', 'w')
    data = open("d:/gcj/A-large.in", "r")
    #data = open("d:/gcj/in.txt", "r")
    N = int(data.readline())
    for case in range(1, N + 1):
        n, k = getInts()
        if (("0"*30)+bin(k)[2:])[-n:]=='1'*n:
            ans="ON"
        else: 
            ans="OFF"
        s = "Case #%d: %s\n"%(case, ans)
        print s,
        output.write(s)
    print time()-start_time	  