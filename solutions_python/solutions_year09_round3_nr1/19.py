from gcjt import *
l = '1023456789abcdefghijklmnopqrstuvwxyz'
for t in tests():
      s,d,u,p = t.rl().replace('\n',''),{},[],0
      for c in s:
            if c not in d:
                  d[c] = l[p]
                  p+=1
            u.append(d[c])
      if p==1:p=2
      t.answer(int(''.join(u),p))
                  
                  
      
