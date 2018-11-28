def printout(n, v):
  print "Case #" + str(n) + ": " + str(v)
  
def dictadd(dct, key, val):
  if not dct.has_key(key):
    dct[key] = val
  else:
    dct[key] += val
  
def call():
  n, k = [int(i) for i in raw_input().split()]
  free = {n: 1}
  stallsize = -1
  while k != 0:
    largest = max(free.keys())
    if k > free[largest]:
      k -= free[largest]
      if largest % 2 == 0:
        dictadd(free, largest/2-1, free[largest])
        dictadd(free, largest/2, free[largest])
      else:
        dictadd(free, largest/2, free[largest] * 2)
      del free[largest]
    else:
      stallsize = largest
      k = 0
  return str(stallsize/2) + " " + str(stallsize/2 - (1 if stallsize%2 == 0 else 0))
  
t = int(raw_input())
for ii in xrange(t):
  printout(ii+1, call())