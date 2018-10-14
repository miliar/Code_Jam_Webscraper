#!/usr/bin/python
import sys

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



def io(ifp):
  if not ifp:
    ifp = 'input'
  with open(ifp, 'r') as inf:
    with open('output','w') as of:
      lno = 0
      l = inf.readline()[:-1]
      while l:
        lno += 1 
        # Code begins here
        if lno > 1:
          R = int(l.split()[0])
          m = []
          rind = 0
          while rind < R:
            l = inf.readline()[:-1]
            m.append([c for c in l])
            rind += 1
          o = solve(m)
          ol = "Case #%d:" % (lno - 1)
          print o
          if o:
            of.write(str(ol) + '\n')
            ol = ''
            for line in m:
              ol = ''
              for c in line:
                ol += c
              of.write(ol + '\n')
          else:
            of.write(str(ol) + '\n')
            of.write('Impossible' + '\n')
            
        l = inf.readline()[:-1]

def solve(m):
  print m
  ln = len(m)
  for i in range(ln):
    for j in range(len(m[i])):
      if m[i][j] == "#" and i < ln -1 and j < len(m[i]) -1 and m[i][j+1] == "#" and m[i+1][j] =="#" and m[i+1][j+1] =="#":
        m[i][j] = "/"
        m[i][j+1] = "\\"
        m[i+1][j] = "\\"
        m[i+1][j+1] = "/"
  for i in range(ln):
    for j in range(len(m[i])):
      if m[i][j] == "#":
        print m[i][j]
        return None
  return m
        

if __name__ == "__main__":
  if len(sys.argv) > 1:
    io(sys.argv[1])
  else:
    io('')



