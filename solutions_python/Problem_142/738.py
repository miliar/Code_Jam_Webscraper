import itertools

def read_ints():
  return map(int, raw_input().split())

def moves(ints):
  avg = int(round(sum(ints) / float(len(ints))))
  total = sum([abs(i-avg) for i in ints])
  return total

def seq(x):
  return [ch for ch,v in [pair for pair in x]]

def solve(strings):
  x = [[(k, len([i for i in v]))
	  for k, v in itertools.groupby(s)]
         for s in strings]
  if not all([len(i) == len(x[0]) for i in x]):
    return -1
  #print x
  #if not 1==len(set(seq(x))):
  #  return -1
  ans = 0
  for i in range(len(x[0])):
    chars = [y[i][0] for y in x]
    if not len(set(chars))==1:
      return -1
    ints = [y[i][1] for y in x]
    ans += moves(ints)
    
  return ans

for test in range(1, int(raw_input()) + 1):
  N, = read_ints()
  strings = [raw_input() for i in range(N)]
  sol = solve(strings)
  if sol == -1:
    sol = "Fegla Won"
  print "Case #%d:" % (test,),
  print sol
