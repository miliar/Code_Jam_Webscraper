#!/usr/bin/python

# Returns gcd of a,b
def gcd(a, b):
  while b != 0:
    t = b
    b = a % b
    a = t
  return a

# Returns (found, index found or to be inserted)
def bs(l, v, s, e):
  if e < s:
    return (False, s - 1)
  m = (s + e) / 2
  if l[m] == v:
    return (True, m)
  elif v < l[m] :
    return bs(l,v,s,m-1)
  else:
    return bs(l,v,m+1,e)

# Sum of permutations
def permute(l, i):
  cl = l[i]
  tsum=0
  for c in cl:
    if i == 0:
      tsum += 1
    else:#conditions here
      tsum +=permute(l,i - 1)
  return tsum



# here
def getl(l,c):
  rl=[]
  for i in range(len(l)):
    if l[i] == c:
      rl.append(int(l[i+1]))
  return rl

def io():
  with open('input', 'r') as inf:
    with open('output','w') as of:
      lno = 0
      for l in inf:
        lno += 1 
        # Code begins here
        if lno > 1:
          ls = l.split()
          ls = ls[1:]
          lo = getl(ls, 'O')
          lb = getl(ls, 'B')

          o = solve(ls, lo,lb)
          print o
          ol = "Case #%d: %d" % (lno - 1, o)
          of.write(str(ol) + '\n')


def getnext(l, i):
  c = 0
  if i == 0:
    c = l[0] - 1
  else:
    c = abs(l[i] - l[i-1])
  return c
  
def getnmv(l, i):
  return l[2 * i]

def solve(l, lo, lb):
  io = 0
  ib = 0
  tc = 0
  co = 0
  cb = 0
  
  i = 0
  lenby2 = len(l)/2
  while i < lenby2:
    c = getnmv(l, i)
    if (c == 'O'):
      tco = getnext(lo, io)
      io += 1      

      if tco <= cb:
        tco = 0
      else :
        tco = tco - cb

      tc += 1 + tco
      cb = 0
      co  += 1 + tco
    else:
      tcb = getnext(lb, ib)
      ib += 1
      
      if tcb <= co:
        tcb = 0
      else :
        tcb = tcb - co

      tc += 1 + tcb
      co = 0
      cb += 1 + tcb
    i += 1
  return tc

if __name__ == "__main__":
  io()



