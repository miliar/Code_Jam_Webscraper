from tqdm import tqdm
from xheap import OrderHeap
from collections import defaultdict

def solve():
  N, K = map(int, input().split())
  max_heap = OrderHeap([], lambda key: -key)

  unique = set()
  cnt = defaultdict(int)

  max_heap.push(N)
  cnt[N] = 1

  while len(max_heap) > 0:
    val = max_heap.pop()
    nr = cnt[val]

    if K <= nr:
      return (val - 1 - (val-1)//2, (val - 1) // 2)
    else:
      K -= nr

    unique.add(val)
    l = [(val-1)//2, val - 1 - (val-1)//2]
    for el in l:
      if el:
        if cnt[el] is 0:
          max_heap.push(el)
        cnt[el] += nr

  #print (N, K, max_heap)

if __name__ == "__main__":
  #test()
  T = int(input())
  for t in tqdm(range(1, T + 1)):
    solution = solve()
    print ("Case #{}: {} {}".format(t, solution[0], solution[1]))
