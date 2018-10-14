from gcjt import *
for t in tests():
      s = ['0']+[c for c in t.rl().replace('\n','')]
      ll = [0]*10
      found = False
      for p in range(len(s)-1,-1,-1):
            u = int(s[p])
            for i in range(u+1,10):
                  if ll[i]:
                        s[p]=str(i)
                        ll[i]-=1
                        ll[u]+=1
                        found = True
                        break
            if found: break
            ll[u]+=1
      s = s[:p+1]
      if s[0]=='0':s=s[1:]
      s = ''.join(s)+''.join([str(i)*ll[i] for i in range(10)])
      t.write(s)
