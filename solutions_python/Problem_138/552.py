import sys 
import string
from collections import *

#playing war optimally:
#naomi chooses a block 
#naomi chooses a block ken can beat then ken chooses the smallest block he has to beat naomi's
#naomi chooses a block ken can't beat then ken chooses the smallest block he has.
#so naomi gets as many points as she has blocks that are heavier than ken's heaviest block. 

#playing deceitful war: 

def intersect(a, b):
	return list(set(a) & set(b))

def fl(x):
    return float(x)

f = open(sys.argv[1])

T = int(f.readline())
for c in xrange(1, T+1): 
 n = int(f.readline())
#the score for playing war 
 blocksnz = f.readline().strip().split(' ')
 blockskz = f.readline().strip().split(' ')
 blocksn = sorted(map(fl, blocksnz))
 blocksk = sorted(map(fl, blockskz))
 wscore = 0
 while len(blocksn)>0 and len(blocksk)>0:
  nb = blocksn[0]
  blocksn.remove(nb)
  if nb>max(blocksk):
   blocksk.remove(min(blocksk))
   wscore += 1
  else:
   kb = len(blocksk)-1
   while kb>0 and blocksk[kb-1]>nb:
    kb -= 1
   blocksk.remove(blocksk[kb])
#the score for deceitfl war
 blocksn = map(fl, blocksnz)
 blocksk = map(fl, blockskz)
 blocksn.sort()
 blocksk.sort()
 dscore = 0
 while len(blocksn)>0 and len(blocksk)>0:
  if max(blocksk)<max(blocksn):
   bb = 0
   for i in range(0, len(blocksn)):
    if blocksn[i]<min(blocksk):
      bb += 1
   blocksn.remove(blocksn[bb])
   blocksk.remove(min(blocksk))
   dscore += 1
  elif min(blocksn)>min(blocksk):
   blocksk.remove(min(blocksk))
   blocksn.remove(min(blocksn))
   dscore += 1
  else:
   blocksn.remove(min(blocksn))
   blocksk.remove(max(blocksk))
 print 'Case #' + str(c) + ': ' + str(dscore) + ' ' + str(wscore)

