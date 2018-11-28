
def gcd(a, b):
  a, b = sorted([a,b])
  while b%a != 0:
    a, b = b%a, a
  return a

def lcm(a, b):
  return a * b / gcd(a,b)

T = input()
for k in range(1,T+1):
  N, L, H = map(int, raw_input().split())
  ns = map(int, raw_input().split())
  ns.sort()
  for i in range(L, H+1):
    mods = True
    for n in ns:
      if (max(n,i) % min(n,i) != 0):
         mods = False
         break
    else:
      print "Case #%d: %d" % (k, i)
      mods = True
    if mods:
      break
  else:
    print "Case #%d: NO" % k
  #print ns, i, L, H
