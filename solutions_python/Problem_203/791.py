from collections import defaultdict

def fill(pos, lst,d,cnt,lets,nchar,ans):
  if pos == cnt and check(lst,lets,nchar):
    ans = lst
    return ans

  if pos == cnt:
    return None
           
  i, j = d[pos]

  for ch in lets:
    lst[i][j] = ch

    tmp = fill(pos+1,lst,d,cnt,lets,nchar,ans)
    if tmp != None:
      return tmp
  return None
  
def check(lst, lets, nchar):
  uDict = defaultdict(lambda:1000)
  rDict = defaultdict(lambda:1000)
  bDict = defaultdict(int)
  lDict = defaultdict(int)
  charD = defaultdict(bool)
  
  for l in range( len(lst) ):
    for k in range(nchar):
      ch = lst[l][k]
      uDict[ch] = min(uDict[ch],l)
      bDict[ch] = max(bDict[ch],l)
      rDict[ch] = min(rDict[ch],k)
      lDict[ch] = max(lDict[ch],k)
      charD[ch] = True

  for ch in uDict:
    for i in range(uDict[ch],bDict[ch]+1):
      for j in range(rDict[ch],lDict[ch]+1):
        if charD[ch] and lst[i][j] != ch:
          return False
  return True

tc = int(raw_input())  # read a line with a single integer

for ii in xrange(1, tc + 1):
  nrow, nchar = map(int, raw_input().split(" "))
  lst = [list() for i in range(nrow)]
  for i in range(nrow):
    lst[i] = list(raw_input())

  lets = set()

  cnt = 0

  d = dict()
  
  for i in range(nrow):
    for j in range(nchar):
      x = lst[i]
      if x[j] != '?':
        lets.add(x[j])
      else:
        d[ cnt ] = (i,j)
        cnt += 1

  ans = None
  if len(d) > 0:
    ans2 = fill(0, lst,d,cnt,lets,nchar,ans)
  else:
    ans2 = lst
        
  print "Case #{}:".format(ii)
  for i in ans2:
    print ''.join(i)

