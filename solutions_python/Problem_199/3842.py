t = int(raw_input())
for row in xrange(1, t + 1):
  n, k = [st for st in raw_input().split(" ")]
  s=len(n)
  k=int(k)
  l=s-k+1
  f=[]
  m=[]
  ans=[]
  for i in range(s):
       f.append(0)
       m.append(0)
       ans.append(0)
  c=0
  for i in xrange(0,s):
      if n[i]=='+':
         m[c]=0
      else:
          m[c]=1
      c+=1

  impossible=0
  for i in xrange(1,s+1):
       sigma=0       
       for j in xrange(i-k,i-1):
              if (j>=0):
                sigma+=f[j]
       sigma+=m[i-1]
       sigma=sigma%2
       ans[i-1]=sigma
       if i>l:
         f[i-1]=0
       else:
         if sigma==0:
             f[i-1]=0
         else:
             f[i-1]=1
             ans[i-1]+=1
       ans[i-1]=ans[i-1]%2
       impossible+=ans[i-1]
  res=0
  for x in xrange(0,l):
      res+=f[x]
  #print ans
  if impossible==0:    
    print "Case #{}: {}".format(row , res)
  else:
    print "Case #{}: {}".format(row ,'IMPOSSIBLE')
  # check out .format's specification for more formatting options
raw_input()
