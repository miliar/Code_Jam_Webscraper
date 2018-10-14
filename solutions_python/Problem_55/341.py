#import psyco
#psyco.full()

class memoize:
  def __init__(self, function):
    self.function = function
    self.mem = {}
  def __call__(self, *args):
      if args not in self.mem:
        self.mem[args] = self.function(*args)
      return self.mem[args]
	  

      
      
def solve(R, k, N, groups):#R rounds, K space on rollercoaster
    #@memoize
    def ride(i): #first in line is group #i
        s = 0
        for _ in range(N): # no more than N groups
            g = groups[i]
            if s+g>k:
                break
            s+=g
            i= (i+1)%N
        return (i, s)
    
    next = [-1]*N
    euro = [0]*N
    j = 0
    while next[j]==-1:
        t,s = ride(j)
        euro[j] = s
        next[j] = t
        j = t
       
    #print("cycle detected (j-> ... -> j)")
    #print next
    #print euro
    #print j
    
    cycle_reward = euro[j]
    cycle_length = 1
    t = next[j]
    while t!=j:
        cycle_reward += euro[t]
        cycle_length += 1
        t = next[t]
    
    sum=0
    
    #print("done pre-processing!")
    #print cycle_reward
    #print cycle_length
    #print j
    
    #part 1: before cycle
    t=0
    r=0
    while r<R and t!=j:
        sum+=euro[t]
        t = next[t]
        r+=1
     
    #part 2: the cycle
    num_loops=(R-r)//cycle_length
    sum += num_loops*cycle_reward
    r+= num_loops * cycle_length
    
    #part 3: finish
    while r<R:
        sum+=euro[t]
        t = next[t]
        r+=1
    
    return sum
    

      
from time import time
if __name__ == "__main__":
    def getInts():
        return map(int, data.readline().rstrip('\n').split(' '))
    start_time=time()
    output = open('d:/gcj/output', 'w')
    
    data = open("d:/gcj/C-large.in", "r")
    #data = open("d:/gcj/C-small-attempt0.in", "r")    
    #data = open("d:/gcj/in.txt", "r")
    for case in range(1, int(data.readline()) + 1):
        R, k, N = getInts()
        #R = 10**5
        groups = getInts()
        y = solve(R, k, N, groups)
        s = "Case #%d: %s\n"%(case, y)
        print s,
        output.write(s)
    print time()-start_time	  