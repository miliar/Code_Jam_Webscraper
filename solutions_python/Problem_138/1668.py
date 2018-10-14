Ntest=input()
import copy
ans=[]
for i in xrange(Ntest):
  n=input()
  naomi=map(float,raw_input().split())
  ken=map(float,raw_input().split())
  naomi.sort()
  naomi2=copy.deepcopy(naomi)
  ken2=copy.deepcopy(ken)
  ken.sort()
  naomi2.sort()
  ken2.sort()
  x=0
  y=0
  for j in xrange(n):
    for k in xrange(len(ken)):
      if naomi[j]>ken[k]:
        del ken[k]
        x+=1
        break
    for z in xrange(len(naomi2)):
      if ken2[j]>naomi2[z]:
        del naomi2[z]
        y+=1
        break
  ans.append("Case #"+str(i+1)+": "+str(x)+" "+str(n-y))
for i in ans:
  print i
  
