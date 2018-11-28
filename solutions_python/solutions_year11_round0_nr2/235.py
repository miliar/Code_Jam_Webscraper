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

def solve(combine,oppose,invoke):
    #print
    #print combine
    #print oppose
    #print invoke
    ans=[]
    for i in invoke:
        if ans==[]:
            ans.append(i)
        elif i+ans[-1] in combine:
            ans[-1]=combine[i+ans[-1]]
        elif i in oppose and oppose[i] in ans:
            ans=[]
        else:
            ans.append(i)
    
    return ans

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
        line = data.readline().rstrip('\n').split(' ')
        def next():
            return line.pop(0)
        C = int(next())
        combine={}
        for _ in range(C):
            x = next()
            combine[x[0]+x[1]] = x[2]
            combine[x[1]+x[0]] = x[2]
        
        D = int(next())
        oppose={}
        for _ in range(D):
            x = next()
            oppose[x[0]] = x[1]
            oppose[x[1]] = x[0]
                
        N = int(next())
        invoke=next()
        
        ans = solve(combine,oppose,invoke)
        ans = '[' + ", ".join(ans) +']'
        s = "Case #%d: %s\n"%(case, ans)
        print s,
        output.write(s)
    print "Total time: %d msec"%(1000*(time()-start_time))