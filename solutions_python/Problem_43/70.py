#!/usr/bin/python

###############################################################################
#
# Google Code Jam 2009 - Round 1C : A
#
# Author: Andres Ayala
# email: killerrex@gmail.com
# License: GPL3
#
# Usage:
#    ./r1C_a.py "input_file"  > output_file
#
###############################################################################

from sys import argv


def lreplace(L, Lref, i, nxt):
  c = Lref[i]
  for n in xrange(i,len(Lref)):
    if Lref[n]==c:
      L[n] = nxt
    
def replace_next(L, Lref, k, done, nxt):
  i=k
  while (Lref[i] in done):
    i+=1
    if i==len(Lref):
      return -1  
  lreplace(L, Lref, i, nxt)
  return i

def get_min_base(L):
  """
  Return the minimum base valid
  (Any superior base will produce greater numbers)
  """
  base = '0123456789abcdefghijklmnopqrstuvwxyz'
  
  # Note: 0 is the only number that starts (and ends) with 0
  if len(L) ==1:
    return 1
    
  Lnew = list(L)
  # Assign always the 1 to the first char
  lreplace(Lnew, L, 0, '1')
  done = L[0]
  # And 0 to the next char
  nxt = replace_next(Lnew, L, 1, L[0], '0')
  if (nxt>-1):
    done = done + L[nxt]
    i = len(done)
  else:
    done='01'
  
  while (nxt>-1) and (nxt<len(L)-1):
    nxt = replace_next(Lnew, L, nxt+1, done, base[i])
    if nxt==-1:
      break
    else:
      done = done + L[nxt]
      i+=1
  return int(''.join(Lnew), len(done))

###############################################################################
def batch(name):
  """ Read the input and print the output :-D"""
  
  fd = open(name,"r")
  T = int(fd.readline())

  i=1
  for k in xrange(T):
    line = fd.readline().strip()
    b = get_min_base(line)
    print "Case #%d: %s" % (i, b)
    i +=1

  fd.close()





###############################################################################
if __name__ == '__main__':
  if len(argv)==2:
    batch(argv[1])
  else:
    print "Usage: ", argv[0], " input_file"

