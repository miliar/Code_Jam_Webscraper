# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for row in xrange(1, t + 1):
  n, k = [st for st in raw_input().split(" ")]  # read a list of integers, 2 in this case
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

  impos=0
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
       impos+=ans[i-1]
  res=0
  for x in xrange(0,l):
      res+=f[x]
  #print ans
  if impos==0:    
    print "Case #{}: {}".format(row , res)
  else:
    print "Case #{}: {}".format(row ,'IMPOSSIBLE')
  # check out .format's specification for more formatting options
raw_input()
