import itertools

mulMap = {
  '1': {'1': '1','i': 'i','j': 'j','k': 'k'},
  'i': {'1': 'i','i': '-1','j': 'k','k': '-j'},
  'j': {'1': 'j','i': '-k','j': '-1','k': 'i'},
  'k': {'1': 'k','i': 'j','j': '-i','k': '-1'}
}

def mul(x, y):
  sign = '-' if len(x)*len(y) == 2 else ''
  res = sign + mulMap[x[-1]][y[-1]]
  return res[-1] if len(res)>2 else res

ansStr = "Case #{}: {}"
tc = int(input())
T = tc
while tc > 0:
  tc -= 1
  [l, t] = map(int, raw_input().split())
  inp = raw_input()
  inp = inp * t
 
  # memorize[i] = mul of 0 to index i including
  memorize = dict()
  
  def mulList(ll, rl):
    # ll to rl (Includes ll and rl)
    lhm = memorize[ll-1]
    tot = memorize[rl]
    k = '1'
    for key in mulMap[lhm[-1]].keys():
      if mulMap[lhm[-1]][key] == tot[-1]:
        k = key
        break
    if mul(lhm, k) == tot:
      return k
    else:
      return '-' + k

  # Fetch i stops
  iStops = []
  iPrev = '1'
  for i in xrange(l*t):
    iCur = mul(iPrev, inp[i])
    memorize[i] = iCur
    if iCur == 'i':
      iStops.append(i)
    iPrev = iCur
  if len(iStops) == 0:
    print ansStr.format(T-tc, "NO")
    continue

  # Fetch k stops
  kStops = []
  kPrev = '1'
  for k in xrange(l*t-1, -1, -1):
    kCur = mul(inp[k], kPrev)
    if kCur == 'k':
      kStops.append(k)
    kPrev = kCur
  if len(kStops) == 0:
    print ansStr.format(T-tc, "NO")
    continue

  flag = False
  for (iInd, kInd) in itertools.product(iStops, kStops):
    if iInd < kInd - 1 and mulList(iInd+1, kInd-1) == 'j':
      flag = True
      break

  if flag:
    print ansStr.format(T-tc, "YES")
  else:
    print ansStr.format(T-tc, "NO")
