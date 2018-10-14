def printout(n, v):
  print "Case #" + str(n) + ": " + str(v)
  
def dictadd(dct, key, val):
  if not dct.has_key(key):
    dct[key] = val
  else:
    dct[key] += val
  
def call():
  imp = 'IMPOSSIBLE'
  data = [int(i) for i in raw_input().split()]
  all = data[0]
  r, o, y, g, b, v = data[1:]
  counts = [[r, 'R'], [y, 'Y'], [b, 'B']]
  counts.sort()
  counts.reverse()
  list = [' ']
  for i in range(all):
    maxpos = -1
    maxval = -1
    for i,j in enumerate(counts):
      if j[1] != list[-1] and maxval < j[0]:
        maxpos = i
        maxval = j[0]
    if maxval == 0:
      return imp
    counts[maxpos][0] -= 1
    list.append(counts[maxpos][1])
  list = list[1:]
  if list[0] == list[-1] and len(list) > 1:
    return imp
  return ''.join(list)
  
  
  
t = int(raw_input())
for ii in xrange(t):
  printout(ii+1, call())