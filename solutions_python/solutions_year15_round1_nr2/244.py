debug = True

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

def lcm(lst):
  product = 1
  for item in lst:
    product *= item
  return product / reduce(gcd, lst)

T = int(raw_input())
for case in range(T):
  B, N = map(int, raw_input().split())
  M = map(int, raw_input().split())

  l = lcm(M)
  full_loop_count = sum(l/m for m in M)  # how many can be handled in a full loop
  N %= full_loop_count
  if N == 0:
    N += full_loop_count

  barbers = M[:]
  while True:
    free_barbers = [m == b for m, b in zip(M, barbers)]
    while True in free_barbers:
      free_barber = free_barbers.index(True)
      free_barbers[free_barber] = False
      N -= 1
      if N == 0:
        answer = free_barber + 1
        break
    if N == 0:
      break
    barbers = [barber if free_barbers[i] else barber - 1 for i, barber in enumerate(barbers)]
    barbers = [barber if barber else M[i] for (i, barber) in enumerate(barbers)]
  print "Case #{}: {}".format(case + 1, answer)
