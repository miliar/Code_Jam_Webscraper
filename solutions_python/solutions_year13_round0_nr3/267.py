LIST = [1,4,9]
# LIST = [1,2,3]

class IAMException(Exception):
  pass

def tenexp(n):
  r = 1
  for i in range(0, n):
    r *= 10
  return r

def ispal(sN):
  return sN == sN[::-1]

def checkpal(spal):
  pal = int(spal)
  palsq = pal * pal
  spalsq = str(palsq)
  if ispal(spalsq):
    LIST.append(int(spalsq))
    # LIST.append(int(pal))
    if len(spalsq) > 105:
      raise IAMException()

def checknum(si):
  pal1 = si + si[::-1]
  checkpal(pal1)
  if len(si) > 1:
    pal2 = si + si[:-1][::-1]
    checkpal(pal2)

if False:
  # this was used to generate the listing 'listc'
  try:
    i = 1
    while True:
      si = bin(i)[2:]
      checknum(si)
      if si.count('1') <= 2:
        checknum('2' + si[1:])
        checknum(si[:-1] + '2')
      i += 1
  except IAMException:
    pass

  LIST = list(set(LIST))
  LIST.sort()

  for n in LIST:
    print str(n) + ","
else:
  ns = []
  for line in open('listc2').readlines():
    ns.append( int(line.strip()) )

  import sys
  import math
  s = sys.stdin
  T = int(s.readline().strip())
  for cs in range(1, T+1):
    inputs = s.readline().strip().split(' ')
    A = int(inputs[0])
    B = int(inputs[1])
    xxx = [x for x in ns if A <= x <= B]
    cnt = len(xxx)
    print 'Case #%d: %d' % (cs, cnt)

