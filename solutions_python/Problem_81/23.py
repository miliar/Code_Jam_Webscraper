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

  def clear(self):
      self.memoized = {}

def gcd(a,b):
    while b: a,b = b, a%b
    return a
    
def abs(x):
    if x<0: return -x
    return x
    
def maxarg(f, args):
    max=-1
    for a in args:
        x = f(a)
        if x>max:
            best=a
            max=x
    return best

def solve():
    num=[sum(1.0 for x in R[i] if x!=0) for i in range(n)]
    WP  =[sum(1.0 for x in R[i] if x==1)/num[i] for i in range(n)]
    
    @memoize
    def wp(i,e):
        if R[i][e]==0:
            return WP[i]
        w = sum(1.0 for k in range(n) if R[i][k]==1 and k!=e)
        #print "wp:", i, e, w, num[i]-1, "->", w / (num[i]-1)
        return w / (num[i]-1)

    #print "num ",num
    #print "WP  ",WP
    
    #print "$$$ ", sum(wp(k,n-1) for k in range(n) if R[i][k]), num[n-1]
    OWP=[sum(wp(k,i) for k in range(n) if R[i][k]) / num[i] for i in range(n)]
   # print "OWP ",OWP
    #for i in range(n):
     #   OWP[i]= num_played / won
    OOWP=[sum(OWP[k] for k in range(n) if R[i][k]) / num[i] for i in range(n)]
   # print "OOWP",OOWP
    
    RPI=[0.25*WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i] for i in range(n)]
   # print RPI
    return RPI

from time import time
if __name__ == "__main__":
    def getInts(): return map(int, input.readline().rstrip('\n').split(' '))
    def getFloats(): return map(float, input.readline().rstrip('\n').split(' '))
    def getMatrix(rows): return [getInts() for _ in range(rows)]
    def getString(): return input.readline().rstrip('\n')
    input, output = open("in", "r"), open('output', 'w')
    start_time=time()
    for case in range(1, int(input.readline()) + 1):
        n = getInts()[0]
        R=[]
        for _ in range(n):
            line = input.readline().rstrip('\n')
            #print line
            r=[]
            for l in line:
                if l=='1': 
                    r.append(1)
                if l=='0':
                    r.append(-1)
                if l=='.':
                    r.append(0)
            R.append(r)
        ans= "\n".join(map(str, solve()))
        s="Case #%d: \n%s\n" % (case,  ans)
        print s
        output.write(s)

    print time()-start_time
