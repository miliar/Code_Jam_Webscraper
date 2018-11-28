def isTidy(n):
  s = str(n)
  prv = int(s[0])
  for i in xrange(1, len(s)):
    if prv > int(s[i]):
      return False
    else:
      prv = int(s[i])  
  return True    

def dec(n):
  s = str(n)

def lastTidies(l, r):
  if isTidy(l + r):
    return l + r
  else:
    if int(l) > int(r[0]):
      return str(int(l)-1) + ('9'*len(r))  
    elif len(r) > 1:
      r2 = lastTidies(r[0], r[1:])
      if(not isTidy(l+r2)):
        return str(int(l)-1) + ('9'*len(r))  
      else:  
        return l + r2
    else:
      return r  

def lastTidy(n):
  s = str(n)
  tidy = -1
  if len(s) > 1:
    tidy = int(lastTidies(s[0], s[1:]))
  else: 
    tidy = int(s)

  if(not isTidy(tidy)):
    tidy = '9'*(len(str(tidy))-1)
  return tidy  

fin = open('./B/B-large.in', "r")
fout = open('./B/B-large.out', "w")

t = int(fin.readline())

for i in xrange(1, t + 1):
  n = int(fin.readline())
  fout.write("Case #{}: {}\n".format(i, str(lastTidy(n))))
  
