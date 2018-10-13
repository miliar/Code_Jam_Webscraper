import heapq
import math
def best_height(pancakes, K, max_radius, exclude):
  #filtered = filter(lambda i, pancake: pancake[0] <= max_radius and i != exclude, xrange(len(pancakes)))
  filtered = [pancakes[i]  for i in xrange(len(pancakes)) if (pancakes[i][0] <= max_radius and i != exclude)]
  nlarge = heapq.nlargest(K, filtered, lambda pancake: pancake[0] * pancake[1])
  flts = [pancake[0] * pancake[1] for pancake in nlarge]
  return 2 * math.pi * sum(flts)

def solve(N, K, pancakes):
  best = 0.0
  for i, max_pancake in enumerate(pancakes):
    me = math.pi * (max_pancake[0]**2) + 2 * math.pi * max_pancake[0] * max_pancake[1]
    height = best_height(pancakes, K - 1, max_pancake[0], i)
    current = me + height
    best = max(best, current)
    
  return best
  
def ints(lst):
  return [int(x) for x in lst]
      
def main():
  name = "A-large"
  lines = open(name+'.in').read().split("\n")
  out = []
  num_tests = int(lines[0])
  spot = 1
  for test in xrange(num_tests):
    parts = lines[spot].split(" ")
    N = int(parts[0])
    K = int(parts[1])
    pancakes_raw = lines[spot+1:spot+1+N]
    pancakes = [ints(x.split(" ")) for x in pancakes_raw]
    pancakes.sort(key = lambda x:x[0], reverse=True)
    res = "Case #%d: %.9f" % (test+1, solve(N,K,pancakes))
    out.append(res)
    print(res)
    spot += (1+N)

  open(name+'.out','w').write("\n".join(out))
    
main()