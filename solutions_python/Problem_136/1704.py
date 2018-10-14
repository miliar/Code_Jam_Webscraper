Ntest=input()
ans1=[]
for i in xrange(Ntest):
  ans=[]
  C,F,X=map(float,raw_input().split())
  click=2
  j=0
  while j<=X:
    click=2
    sec=0.0
    for k in xrange(j):
      sec+=C/click
      click+=F
    sec+=X/click
    ans.append(sec)
    j+=1
  ans1.append('Case #'+str(i+1)+': '+str("%.7f" %min(ans)))
for i in ans1:
  print i

  
