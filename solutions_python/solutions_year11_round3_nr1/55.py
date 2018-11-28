#!/usr/bin/python
from numpy import *
from pylab import find

def readLines(fname):
  with open(fname,'r') as f :
    lines = r_[[ s[:-1] for s in f.readlines() ]]
    return lines

  return None

def load(fname):
  txt = readLines(fname)
  nc  = int(txt[0])
  out = []

  p = 1

  for i in range(nc):
    h,w = r_[txt[p].split(' ')].astype('int')
    pic = txt[(p+1):(p+1+h)]
    p = p+1+h
    out.append(pic)

  return out

def st2ar(txt):
  return r_[ [ ord(c) for c in txt ] ]

def pic2text(pic):
  ll = []
  for p in pic:
    ll.append(''.join([ chr(x) for x in p]))
  return '\n'.join(ll)
  

def solve(p):
  txt = p
  pic = c_[[ st2ar(t) for t in txt ]]
  #print pic

  h,w = pic.shape

  for i in range(h):
      for j in range(w):
          if pic[i,j] == 35 :
              if i+1 >= h or j+1 >= w:
                  return None
              if pic[i,j+1] != 35:
                  return None
              if pic[i+1,j+1] != 35:
                  return None
              if pic[i+1,j] != 35:
                  return None

              pic[i,j] = pic[i+1,j+1] = 47
              pic[i,j+1] = pic[i+1,j] = 92

  return pic2text(pic)
  #return None


if __name__ == "__main__":
  import sys
  
  problem = load(sys.argv[1])
   
  for p,i in zip(problem,range(len(problem))):
    r = solve(p)

    print "Case #%d:" % (i+1)

    if r == None:
      print "Impossible"
    else:
      print r
