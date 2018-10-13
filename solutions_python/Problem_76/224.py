#<boilerplate>
def alloc(size, default = 0): return [default] * size
def alloc2d(r, c, default = 0): return [alloc(c, default)] * r

class memoize:
  def __init__(self, function):
    self.function = function
    self.memoized = {}

  def __call__(self, *args):
      if args not in self.memoized:
        self.memoized[args] = self.function(*args)
      return self.memoized[args]


from bisect import *
def binary_search(a, x, low=0):    
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x, low)
    if i != len(a) and a[i] == x:
        return i
    return None
#</boilerplate>

def xor(a):
    t=0
    for x in a:
        t^=x
    return t

def solve(c):
    #print c
    if xor(c)!=0:
        return "NO"
    return str(sum(c)-min(c))
    
    

from time import time
if __name__ == "__main__":
    def getInts():
        return map(int, data.readline().rstrip('\n').split(' '))

    start_time=time()
    output = open('d:/gcj/output', 'w')
    #data = open("d:/gcj/A-large.in", "r")
    data = open("d:/gcj/in.txt", "r")
    T = int(data.readline())
    for case in range(1, T + 1):
        def next():
            return line.pop(0)
        C = int(data.readline())
        C = getInts()
        
        ans = solve(C)
        s = "Case #%d: %s\n"%(case, ans)
        print s,
        output.write(s)
    print "Total time: %d msec"%(1000*(time()-start_time))