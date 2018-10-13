# -*- coding: utf-8 -*-
# Google Code Jam 2009
# Round1C A

# --- modules ---
import sys

# --- const ---
DBG = False
CSTR = "1023456789abcdefghijklmnopqrstuvwxyz"
# --- funcs ---
def ReadInts():
  line = sys.stdin.readline().rstrip().split()
  return map(int,line)

def dprint(dstr):
  if not DBG: return
  if dstr.__class__ == str:
    sys.stderr.write(dstr+"\n")
  else:
    sys.stderr.write(str(dstr)+"\n")

def NumofChar(line):
  count = 0
  adic = dict()
  ansstr = ""
  for c in line:
    if not adic.has_key(c):
      adic[c] = CSTR[count]
      ansstr += CSTR[count]
      count += 1
    else:
      ansstr += adic[c]
  return (count,ansstr)



# --- main ---
T = ReadInts()[0]
for prob in xrange(1,T+1):
  line = sys.stdin.readline().rstrip()
  anstpl = NumofChar(line)
  dprint(anstpl[0])
  if anstpl[0] == 1:
    ans = long(anstpl[1],2)
  else:
    ans = long(anstpl[1],anstpl[0])
  print "Case #%d: %d"%(prob,ans)
