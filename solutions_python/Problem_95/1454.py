import sys
def solve():
  a = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"
  b = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up"
  
  mappings = {}
  l = len(a)
  for i in range(0,l):
    mappings[a[i]] = b[i]

  mappings['q'] = 'z'
  mappings['z'] = 'q'
#  for i in sorted(mappings.keys()):
#    print i,"-->",mappings[i]

  n = int(raw_input())

  for i in range(0,n):
    a = raw_input()
    b = ''
    for j in a:
      b+=mappings[j]
    print "Case #%d: %s"%(i+1,b)
    

def compute():
  solve()


#compute()
solve()
      





  

