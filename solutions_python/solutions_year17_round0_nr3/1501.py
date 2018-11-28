import heapq
import sys

class MaxHeapObj(object):
  def __init__(self,val): self.val = val
  def __lt__(self,other): return self.val > other.val
  def __eq__(self,other): return self.val == other.val
  def __str__(self): return str(self.val)

class MinHeap(object):
  def __init__(self): self.h = []
  def heappush(self,x): heapq.heappush(self.h,x)
  def heappop(self): return heapq.heappop(self.h)
  def __getitem__(self,i): return self.h[i]
  def __len__(self): return len(self.h)

class MaxHeap(MinHeap):
  def heappush(self,x): heapq.heappush(self.h,MaxHeapObj(x))
  def heappop(self): return heapq.heappop(self.h).val
  def __getitem__(self,i): return self.h[i].val


def Bath_game(i,j):
    maxh = []
    heapq.heappush(maxh,-i)
    for _ in range(j-1):
        vred = -heapq.heappop(maxh)
        mvred = vred//2
        mivred = vred-mvred-1
        heapq.heappush(maxh,-mvred)
        heapq.heappush(maxh,-mivred)
    res = -heapq.heappop(maxh)
    resmax = res//2
    resmin = res-resmax-1
    if resmin < 0:
        resmin = 0
    return resmax, resmin


T = int(sys.stdin.readline())
res = ""
for k in range(T):
    i,j = sys.stdin.readline().split()
    i,j = int(i),int(j)
    rx,rm = Bath_game(i,j)
    res1 = "Case #{0}: {1} {2}".format(k+1,rx,rm)
    print(res1)
    res+= (res1+"\n")
with open("bathres_Csmall2_2.out","w") as izhod:
    izhod.write(res)