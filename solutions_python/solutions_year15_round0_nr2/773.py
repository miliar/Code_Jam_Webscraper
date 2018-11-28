import math

def max_second(lst, mx):
  mx2 = -1

  for i, p in enumerate(pancakes):
    if p > mx2 and p != mx:
      mx2 = p

  return mx2

def equalsplit(n, m):
  d = math.ceil(n / float(m))
  ret = [d for i in range(m - 1)]
  ret.append(n - sum(ret))

  if sum(ret) != n:
    raise "WTF"

  return ret

def breakfast(pancakes):
  minutes = 0

  max_val = max(pancakes)
  max_count = pancakes.count(max_val)

  while True:
    d = -1
    cost = max_val
    for c in range(2, int(math.sqrt(max_val)) + 1):
      #cst = max(math.ceil(max_val / float(c)), max_second(pancakes, max_val)) + max_count * (c - 1)

      P2 = pancakes[:]

      for i, p in enumerate(P2):
        if p == max_val:
          divs = equalsplit(p, c)
          
          P2[i] = divs[0]
          P2.extend(divs[1:])

      cst = breakfast(P2) + max_count * (c - 1)

      if cost >= cst:
        d = c
        cost = cst

    if d == -1:
      break

    for i, p in enumerate(pancakes):
      if p == max_val:
        divs = equalsplit(p, d)
        
        pancakes[i] = divs[0]
        pancakes.extend(divs[1:])

    minutes += max_count * (d - 1)

    max_val = max(pancakes)
    max_count = pancakes.count(max_val)

  return minutes + max(pancakes)

filename = 'B-small-attempt4'
f = open(filename + '.in', 'r')
o = open(filename + '.out', 'w')

T = int(f.readline())

for t in range(T):
  D = int(f.readline())
  pancakes = map(int, f.readline().split())

  #print D, pancakes, breakfast(pancakes)
  o.write('Case #%d: %d\n' % (t + 1, breakfast(pancakes)))
