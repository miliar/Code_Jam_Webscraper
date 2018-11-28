import sys
import heapq
from collections import defaultdict

heap = []
def push(elem):
  heapq.heappush(heap, -elem)

def pop():
   return -heapq.heappop(heap)

def place(x):
  return (x // 2, (x-1) // 2)

def solve_test(inp):
    global heap
    n, k = map(int, inp.readline().split())
    heap = []
    counts = defaultdict(int)
    
    push(n)
    counts[n] = 1
    while k > 0:
      t = pop() 

      #print(t)
      l, r = place(t)
      #print(l,r)
      if not counts[l]: push(l)
      if not counts[r]: push(r)
      counts[l] += counts[t]
      counts[r] += counts[t]
      k -= counts[t]
      counts[t] = 0
    #print(heap)
    return "%d %d" % (l, r)

inp = open(sys.argv[1])
out = open(sys.argv[1].rsplit('.',1)[0]+'.out', 'w')
n_tests = int(inp.readline())
for i in range(n_tests):
    ans = solve_test(inp)
    print("Case #%d: " % (i+1) + ans, file=out)
out.close()