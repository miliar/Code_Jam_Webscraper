import heapq

def mkstate(nstalls):
  return [0] * nstalls

def walk(stalls, n):
  """walk one direction to get distances"""
  moops = [0] * n
  acc = 0
  for (i, v) in enumerate(stalls):
    moops[i] = acc
    if v:
      acc = 0
    else:
      acc += 1
  return moops

def walk_both(stalls):
  """walk in both directions to get two (L,R) distance vectors"""
  n = len(stalls)
  le = walk(stalls, n)
  ri = list(reversed(walk(reversed(stalls), n)))
  return le, ri

assert walk_both(mkstate(4)) == ([0,1,2,3], [3,2,1,0])
assert walk_both([0, 1, 1, 0]) == ([0,1,0,0], [0,0,1,0])
assert walk_both([0, 0, 1, 0]) == ([0,1,2,0], [1,0,1,0])
assert walk_both([1, 0, 1, 1]) == ([0,0,1,0], [1,0,0,0])
assert walk_both([1, 0, 0, 1, 1]) == ([0,0,1,2,0], [2,1,0,0,0])

def eval_stall(stalls, lmoops, rmoops, i):
  """evaluate the desirability of a stall
  returns (-min, -max, i)
  """
  if stalls[i]:
    return (100, 100, i)
  amin = min(lmoops[i], rmoops[i])
  amax = max(lmoops[i], rmoops[i])
  return (-amin, -amax, i)

def eval_stall_test(stalls, i):
  lmoops, rmoops = walk_both(stalls)
  return eval_stall(stalls, lmoops, rmoops, i)

# print eval_stall_test(mkstate(5), 0)
# print eval_stall_test(mkstate(5), 1)
# print eval_stall_test([0, 1, 1, 0], 1)
# print eval_stall_test([0, 1, 1, 0], 3)
# print eval_stall_test([0, 1, 0, 0], 3)
# print [eval_stall_test([0, 1, 0, 0], i) for i in range(4)]

def choose_stall(stalls, lmoops, rmoops):
  """get the index of the best stall"""
  evals = [eval_stall(stalls, lmoops, rmoops, i) for i in xrange(len(lmoops))]
  heapq.heapify(evals)
  best = evals[0]
  return best[-1]

def choose_stall_test(stalls):
  lmoops, rmoops = walk_both(stalls)
  return choose_stall(stalls, lmoops, rmoops)

assert choose_stall_test(mkstate(4)) == 1
assert choose_stall_test(mkstate(5)) == 2
assert choose_stall_test(mkstate(20)) == 9 # made up
assert choose_stall_test([0, 0, 0, 0]) == 1
assert choose_stall_test([0, 1, 0, 0]) == 2
assert choose_stall_test([0, 1, 1, 0]) == 0
assert choose_stall_test([1, 1, 1, 0]) == 3

def add_pooper(stalls, i):
  return stalls[:i] + [1] + stalls[i+1:]

def round_1(stalls):
  """do 1 round
  returns (newstalls, amin, amax)
  """
  lmoops, rmoops = walk_both(stalls)
  i = choose_stall(stalls, lmoops, rmoops)
  amin = min(lmoops[i], rmoops[i])
  amax = max(lmoops[i], rmoops[i])
  return add_pooper(stalls, i), amin, amax

# print round_1(mkstate(4))

def driver(stalls, k):
  for _ in xrange(k):
    newstalls, amin, amax = round_1(stalls)
    stalls = newstalls
  return stalls, amin, amax

def fmtcase(x, casen):
  """Format the output of driver into a case"""
  return "Case #{}: {} {}".format(casen, x[-1], x[-2])

assert driver(mkstate(4), 2) == ([0, 1, 1, 0], 0, 1)
assert driver(mkstate(5), 2) == ([1, 0, 1, 0, 0], 0, 1)
assert driver(mkstate(6), 2) == ([0, 0, 1, 0, 1, 0], 1, 1)
# print fmtcase(driver(mkstate(1000), 1000), 1)
# print fmtcase(driver(mkstate(1000), 1), 1)
# for _ in xrange(100):
#   print fmtcase(driver(mkstate(1000), 1000), 1)

if __name__ == "__main__":
  ncases = int(raw_input())
  for i in xrange(ncases):
    n, k = map(int, raw_input().split(" "))
    print fmtcase(driver(mkstate(n), k), i + 1)
