import sys
sys.setrecursionlimit(100000)
from itertools import combinations, permutations
from math import ceil,floor,factorial

def nchoosek(n,k):
  return factorial(n)/(factorial(n-k)*factorial(k))
    
def strips(s):
  
  snew = s[0]
  cs = [1]
  #~ last = ''
  for i in range(1,len(s)):
    if not s[i] == snew[-1]:
      snew = snew + s[i]
      cs.append(0)
    #~ else:
      #~ if not s[i]==last:
        #~ 
        #~ last = s[i]
    cs[-1]+=1
  return snew , cs
      
def solve():
  
  #~ print tree
  stripeds = []
  counts = []
  for s in tree:
    
    newstr , c = strips(s)
    stripeds.append(newstr)
    counts.append(c)
  
  #~ print stripeds     
  #~ print counts  
  
  allSame = True
  f = stripeds[0]
  for i in range(1,len(stripeds)):
    if not stripeds[i]==f:
      return None
  
  numchars = len(counts[0])
  nums = len(tree)
  
  s = 0
  mins = []
  
  for i in range(numchars):
    news = 0
    for n in range(nums):
      news+=counts[n][i]
    #~ s += ceil(float(news)/float(nums))
    mins.append(news/nums)
    
  #~ print mins  
  
  for i in range(numchars):
    for n in range(nums):
      #~ print i , n , counts[n][i] - mins[i]
      s+= abs(counts[n][i] - mins[i])
  
  return int(s)

T = int(raw_input())

for case in range(T):
  
  N = int(raw_input());
  #~ N , L = map(int,raw_input().split());

  tree = []

  for i in range(N):
    tree.append(raw_input())
  #~ for i in range(N-1):
    #~ edge = map( lambda x : x-1 , map(int,raw_input().split()) )
    #~ tree.append(edge)

  sol = solve()
  
  print 'Case #%d: %s' %(case+1,str(sol) if not sol==None else 'Fegla Won')
    
