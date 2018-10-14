import math
import sys

def countDig(a):
  cDig = 0
  a0 = a
  while a > 0:
    cDig += 1
    a /= 10
  return cDig

def sq(a):
  nStep = 1
  x = 0
  while x*x < a:
    x += nStep
    nStep *= 2
  while x*x > a and nStep != 0:
    if ((x-nStep) * (x-nStep)) >= a:
      x -= nStep
    nStep /= 2
  while x*x < a: x += 1
  while x*x > a: x -= 1
  return x
  
vOk = dict()
for i in range(105): vOk[i] = list()
vOk[1].append("{0:0105}".format(int(1)))
vOk[1].append("{0:0105}".format(int(2)))
vOk[1].append("{0:0105}".format(int(3)))
cOk = len(vOk[1])
mOk = dict()
mOk[1] = 3
bCountOnly = True

def rev(s):
  return s[::-1]
   
def addOnes(s, nNotBef, c1, sFirst, sMid, cDig):
  global bCountOnly
  global cOk, mOk
  L = len(s)
  if c1 > 0 and nNotBef == L:
    return
  if c1 == 0:
    cOk += 1
    if not bCountOnly:
      vOk[cDig].append(sFirst + "".join(s) + sMid + "".join(rev(s)) + sFirst)
    return
  for j in range(nNotBef, L):
    if s[j] != '1':
      s[j] = '1'
      addOnes(s, j+1, c1-1, sFirst, sMid, cDig)
      s[j] = '0'

def multi(nFirst, cDigL, nMid, cDig):
  # 2*m + 2*nFirst*nFirst + nMid*nMid <= 9
  sMid = ""
  if nMid >= 0: sMid = str(nMid)
  m = (9 - nMid*nMid)/2 - nFirst*nFirst
  # We must permute all cDigL combination of digits so that their sum
  # is at most m and then assemble the whole number as
  # nFirst + sLeft + (nMid if >= 0) + rev(sLeft) + nFirst
  s0 = list()
  for i in range(cDigL): s0 += '0'
  for c1 in range(m+1):
    # c1 number of ones
    s = s0
    addOnes(s, 0, c1, str(nFirst), sMid, cDig)

def generate(cDigFrom, cDigTo):
  for cDig in range(cDigFrom, cDigTo+1):
    cOkBef = cOk
    for nFirst in range(1, 3):
      cDigL = (cDig-2)/2
      if (cDig % 2) == 0:
        multi(nFirst, cDigL, -1, cDig)
      else:
        multi(nFirst, cDigL, 0, cDig)
        multi(nFirst, cDigL, 1, cDig)
        multi(nFirst, cDigL, 2, cDig)
    cOkAfter = cOk
    mOk[cDig] = cOkAfter - cOkBef

bCountOnly = False
nGen = 100
generate(2,nGen)
if nGen < 100: sys.stderr.write("warning, generating only up to " + str(nGen) + "\n")
c2 = 0
for cDig in mOk.keys():
  # print cDig, mOk[cDig]
  c2 += mOk[cDig]

fin = open(sys.argv[1])
cTest = int(fin.readline())
for iTest in range(cTest):
  sLinia = fin.readline()
  a0 = int(sLinia.split()[0])
  b0 = int(sLinia.split()[1])
  a = sq(a0)
  b = sq(b0)
  if a*a < a0: a += 1
  assert(a*a >= a0)
  assert((a-1)*(a-1) < a0)
  assert(b*b <= b0)
  assert((b+1)*(b+1) > b0)
  cDigA = countDig(a)
  cDigB = countDig(b)
  cRes = 0
  for cDig in vOk.keys():
    if cDig < cDigA: continue
    if cDig > cDigB: continue
    if cDig > cDigA and cDig < cDigB:
      cRes += mOk[cDig]
      continue
    for sFair in vOk[cDig]:
      p = int(sFair)
      if p >= a and p <= b:
        cRes += 1
  print "Case #" + str(iTest+1) + ": " + str(cRes)
