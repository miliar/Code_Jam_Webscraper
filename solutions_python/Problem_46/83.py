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

  def clear(self):
      self.memoized = {}

def alloc(size, default = 0): return [default] * size
def alloc2(r, c, default = 0): return [alloc(c, default)] * r
def isset(a, bit): return ((a >> bit) & 1) > 0
def dig(c): return ord(c) - 48
def abs(x): 
    if x<0: return -x;
    return x

def area(x1, y1, x2, y2, x3, y3):
    return abs((x3-x1)*(y2-y1) - (x2-x1)*(y3-y1))/2

def bisection(f, lo, hi):
    """
    finds the integer x where f(x)=0.
    assumes f is monotounous.
    """
    while lo < hi:
        mid = (lo+hi)//2
        midval = f(mid)
        if midval < 0:
            lo = mid+1
        elif midval > 0:
            hi = mid
        else:
            return mid
    return None

def minarg(f, args):
    min_val = None
    min_arg = None
    for a in args:
        temp=f(a)
        if min_arg==None or temp<min_val:
            min_val=temp
            min_arg=a
    return min_arg, min_val



#mat[i] = lowest row for the row currently at position i
def solve():
    
    c=0
    for i in range(N):
        #print mat, c
        #print "i=", i
        if mat[i]>i:
            for j in range(i+1, N):
                if mat[j]<=i:
                    #print "replace", i, " with ", j
                    mat.insert(i, mat[j])
                    #print mat
                    del mat[j+1]
                    #mat[j]=None
                    c+=j-i
                    break

    return c

from time import time
if __name__ == "__main__":
    def getInts(): return map(int, input.readline().rstrip('\n').split(' '))
    def getFloats(): return map(float, input.readline().rstrip('\n').split(' '))
    def getMatrix(rows): return [getInts() for _ in range(rows)]
    input, output = open("d:/gcj/in", "r"), open('d:/gcj/output', 'w')
    start_time=time()
    for case in range(1, int(input.readline()) + 1):
        N, = getInts()
        mat=[[int(d) for d in input.readline().rstrip('\n')] for _ in range(N)]
        for i in range(N):
            j=N-1
            while j>0 and mat[i][j]==0:
                j-=1
            mat[i]=j
        s="Case #%d: %d\n" % (case,  solve())
        print s
        output.write(s)

    print time()-start_time

    