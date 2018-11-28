import heapq
import math
from joblib import Parallel, delayed
import multiprocessing


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



def minmax(n):
    min_val = math.floor((n-1)/2)
    max_val = math.ceil( (n-1)/2)
    return [max_val, min_val]


def solve(n, k):
    results = MaxHeap()
    results.heappush(minmax(n)[0])
    results.heappush(minmax(n)[1])

    cntr = 1

    if(k/n > 0.55):
        return [0,0]

    if (k == 1):
        return minmax(n)
    else:
        while(cntr != k):
            cntr += 1
            top = results.heappop()

            minmax_tmp = minmax(top)

            results.heappush(minmax_tmp[0])
            results.heappush(minmax_tmp[1])

        return minmax_tmp



# input and output
t = int(input())  # read a line with a single integer

input_list = []

for i in range(1, t + 1):
  n, k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  input_list.append((n,k))


def processInput(nk_tuple):
    return ((nk_tuple[0], nk_tuple[1]), solve(nk_tuple[0], nk_tuple[1]))

num_cores = multiprocessing.cpu_count()
results = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in input_list)

result_dict = {}
for i in results:
    result_dict[i[0]] = i[1]

for i in range(len(input_list)):
  n = input_list[i][0]
  k = input_list[i][1]
  max_val = max(result_dict[(n, k)])
  min_val = min(result_dict[(n, k)])
  print("Case #{}: {} {}".format(i+1, max_val, min_val))

  #result = solve(n, k)
  #max_val = max(result)
  #min_val = min(result)
  #print("Case #{}: {} {}".format(i, max_val, min_val))
  # check out .format's specification for more formatting options
