#!/usr/bin/env python


def nval(s, n):
  sl = len(s)
  vos = set(['a','o','e','i','u'])
  lasti = -1 
  total = 0
  for i in range(sl):
    if s[i] not in vos:
      conseq = True
      for j in range(i+1, i+n):
        if j >= sl or s[j] in vos:
          conseq = False
          break
      if conseq:
        total = total + (i - lasti) * (sl - i - n + 1)
        #print i, lasti, total
        lasti = i
      
  return total
      
  
def main():
  cases = int(raw_input())
  for case in range(cases):
    case = case + 1
    tups = raw_input().split()
    print 'Case #%d: %d' % (case, nval(tups[0], int(tups[1])))

main()
