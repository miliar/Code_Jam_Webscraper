# python3
import sys

def gcd(a, b):
  while a != 0:
    a, b = b % a, a
  return b

def lcm(a, b):
  return a // gcd(a,b) * b

inp = sys.stdin.readlines()
T = int(inp[0])
for test in range(T):
  [n, l, h] = [int(x) for x in inp[test*2+1].split()]
  xs = [int(x) for x in inp[test*2+2].split()]
  xs.sort()
  gcds,lcms=[],[]
  gcds.append(xs[-1])
  for i in range(1,len(xs)):
    gcds.append(gcd(gcds[-1],xs[-i-1]))
  gcds.reverse()
  lcms.append(xs[0])
  for i in range(1,len(xs)):
    lcms.append(lcm(lcms[-1],xs[i]))
  #print(lcms)
  #print(gcds)
  ok=False
  for i in range(l,h+1):
    if gcds[0] % i == 0:
      r = i
      ok=True
      break
  if not ok:
    for i in range(len(xs)-1):
      if gcds[i+1] % lcms[i] != 0: continue
      #print('g={0} l={1} i={2} [{3}..{4}]'.format(gcds[i+1],lcms[i],i,xs[i],xs[i+1]))
      for r in range(max(l,lcms[i]),min(h,gcds[i+1])+1):
        if r % lcms[i] != 0: continue
        if gcds[i+1] % r != 0: continue
        ok = True
        break
      if ok:
        #print('r={0}'.format(r))
        break
  if not ok:
    r = (l + lcms[-1] - 1) // lcms[-1] * lcms[-1]
    if r <= h:
      ok = True
  if ok:
    print('Case #{0}: {1}'.format(test+1,r))
  else:
    print('Case #{0}: NO'.format(test+1))

