def isUpDown(s):
  m = s.index(max(s))
  for i in range(m):
    if s[i]>s[i+1]:
      return False
  for i in range(m+1,len(s)):
    if s[i]>s[i-1]:
      return False
  return True

def swapDist(s,t):
  ps = [s.index(i) for i in t]
  c = 0
  for i in range(len(ps)):
    for j in range(len(ps)-1):
      if ps[j]>ps[j+1]:
        c+=1
        ps[j],ps[j+1] = ps[j+1],ps[j]
  return c
  
allUpDowns = []
import itertools

for i in range(1,11):
  k = []
  for j in itertools.permutations(range(1,i+1),i):
    if isUpDown(j):
      k.append(j)
  allUpDowns.append(k)


T = int(raw_input())
for t in range(1,T+1):
  N = int(raw_input())
  S = map(int,raw_input().split())
  c = 10**100
  b = []
  k = S[:]
  k.sort()
  S = [k.index(i)+1 for i in S]
  for i in allUpDowns[N-1]:
    #print S,i
    # print swapDist(S,i)
    c = min(c,swapDist(S,i))
    #if c==swapDist(S,i):
    #  b = i
  print "Case #"+str(t)+": "+str(c)
  #print b
