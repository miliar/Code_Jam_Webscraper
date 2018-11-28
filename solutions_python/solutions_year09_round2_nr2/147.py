import psyco
psyco.full()

class memoize:
  def __init__(self, function):
    self.function = function
    self.memoized = {}

  def __call__(self, *args):
      if args not in self.memoized:
        self.memoized[args] = self.function(*args)
      return self.memoized[args]

def m(n):
    d=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while n>0:
        t=n%10
        if t>0:
            d[t]+=1
        n//=10
    return d

def solve(n):
    d=m(n)
    n+=1
    while m(n) != d:
        n+=1
    return n

from time import time
if __name__ == "__main__":
    def getInts():
        return map(int, data.readline().rstrip('\n').split(' '))
    start_time=time()
    output = open('d:/gcj/output', 'w')
    data = open("d:/gcj/in", "r")
    Cases = int(data.readline())
    for case in range(1, Cases + 1):
        n = getInts()
        s="Case #%d: %d" % (case, solve(n[0]))
        print(s)
        output.write(s+"\n")
    print time()-start_time

    