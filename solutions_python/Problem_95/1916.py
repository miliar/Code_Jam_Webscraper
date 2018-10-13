# -*- coding: utf-8 -*-
import sys

_ALPHABETS = [chr(ord("a")+_) for _ in xrange(26)]

def ReadInts(f):
  buf = f.readline().rstrip("\n").split()
  return map(int,buf)

def addmap(strin,strout,alphamap):
  for i in xrange(len(strin)):
    if strin[i] == " " or strin[i] == "\n": continue
    if alphamap.has_key(strin[i]):
      if alphamap[strin[i]] != strout[i]:
        print "Something Wrong!!!!!!!!!"
        print strin[i],alphamap[strin[i]],strout[i]
    else:
      alphamap[strin[i]] = strout[i]
      
      

def makemap():
  fin = open("sample.in")
  fout = open("sample.out")
  T = ReadInts(fin)[0]
  alphamap = {"y":"a","e":"o","q":"z"}
  for t in xrange(T):
    strin = fin.readline().rstrip("\n")
    strout = fout.readline().rstrip("\n")
    addmap(strin,strout,alphamap)
  key = ""
  alphas = _ALPHABETS[:]
  for a in _ALPHABETS:
    if not alphamap.has_key(a):
      key = a
    else:
      alphas.remove(alphamap[a])
  alphamap[key] = alphas[0]
  
  return alphamap

def translate(strin,alphamap):
  ret = ""
  for c in strin:
    if c == " " or c == "\n":
      ret += c
    else:
      ret += alphamap[c]
  return ret
    
def main():
  alphamap = makemap()

  T = ReadInts(sys.stdin)[0]
  for t in xrange(1,T+1):
    line = sys.stdin.readline().rstrip("\n")
    ret = translate(line,alphamap)
    print "Case #%d: %s"%(t,ret)
  return

if __name__ == "__main__":
  main()
  
