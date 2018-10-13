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


def swap(a,i,j):
    temp = a[i]
    a[i]=a[j]
    a[j]=temp

def minimum_swaps_to_sort(a):
    count=0
    d = {}
    for i in range(len(a)):
        d[a[i]]=i
    s=sorted(a)
    for i in range(len(a)):
        #if a[i] is not in it's place
        if a[i]!=s[i]:
            j = d[s[i]] #j = a.index(s[i])
            swap(a,i,j)
            #update dict:
            d[a[i]]=i
            d[a[j]]=j
            count+=1
        #print i, a, count
    return count
    
def solve(a):
    
    s=sorted(a)
    return sum(1 for i in range(len(a)) if a[i]!=s[i])
    

# import random
# c=0.0
# for _ in range(10000):
    # a=[2,3,1]
    # while a!=[1,2,3]:
        # temp=0
        # for i in [1,2,3]:
            # if a[i-1]!=i:
                # temp+=1
        # if temp==2:
            # c+=2
            # break
        
        # random.shuffle(a)
        # c+=1
# print c/10000    

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
        s = "Case #%d: %d.000000\n"%(case, ans)
        print s,
        output.write(s)
    print "Total time: %d msec"%(1000*(time()-start_time))